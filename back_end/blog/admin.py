"""
Create and register the Admin Classes for the Django Admin interface.
"""

from django.contrib import admin
from blog.models import Profile, Post, Tag

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile Admin interface for administration of the 
    Profile model using Django administration.
    model: field - Profile: the user profile model.
    """
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ 
    Tag Admin interface for administration of the
    Tag model using Django administration.
    model: field - Tag: the tag model.
    """
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post Admin interface for administration of the
    Post model using Django administration.
    model: field - Post: the post model.
    list_display: field: the fields we want to display about each post.
    list_filter: field:  we can filter the list of posts by those specific fields.
    list_editable: field: we can edit the list of displayed posts using  those specific fields.
    search_fields: field: the fields we use to search for posts.
    prepopulated_fields: field: the fields that have a slug prepopulated.
    date_hierarchy: field: the fields that we can use for creating a browsable hierarchy with posts.
    save_on_top: field: show a button at the top of the list of posts to save changes.
    """
    model = Post

    list_display = ('id', 
                    'title', 
                    'subtitle', 
                    'slug', 
                    'publish_date', 
                    'published',)
    
    list_filter = ('published',
                   'publish_date',)
    
    list_editable = ('title',
                     'subtitle',
                     'slug',
                     'publish_date',
                     'published',)
    
    search_fields = ('title',
                     'subtitle',
                     'slug',
                     'body',)
    
    prepopulated_fields = {
        'slug':('title', 
                'subtitle'),
    }

    date_hierarchy = 'publish_date'
    save_on_top = True