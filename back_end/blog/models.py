"""
Models that represent the tables into our database.
Profile: model: represents the user profile.
Tag: model: represents the tag associated with a blog post.
"""

from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Profile model that represents the user profile.
    user: field - on to one model: User
    website: field - URL: Website
    bio: field - string: Bio
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.PROTECT,)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the username.
        """
        return self.user.get_username()
    

class Tag(models.Model):
    """
    Tag model for adding tags to a blog post.
    name: field: name of the tag
    """
    name = models.CharField(max_length=50, unique=True)


    def __str__(self) -> str:
        """
        Returns a string representation of the tag name.
        """
        return self.name
    

class Post(models.Model):
    """
    Post model that represents a blog post.
    title: field - string: the title of the post
    subtitle: field - string: the subtitle of the post
    slug: field - slug: the slug of the post
    body: field - text: the body of the post
    meta-description: field - string: the description of the post.
    date_created: field - date: the date when the post was created.
    date_modified: field - date: the date when the post was modified.
    publish_date: field - date: the date when the post was published.
    published: field - boolean: tells whether the post was published or not.
    author: field - ForeignKey:Profile: the user that owns the post.
    tags: field - ManyToMany: Tag: the tags of a post.

    class Meta: metaclass: contain one field ordering: for 
    order the posts in the database in a descending order.
    """
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)


    class Meta:
        """
        Meta class for creating aditional functionality 
        for ordering the creation of the posts, showing the most recent first.
        """
        ordering = ['-publish_date']