"""
GraphQL schema that consists of several classes that are 
each associated with a particular Django model and one to 
specify how to resolve a few important types of queries 
you’ll need in the front end.
Create a corresponding class for each of your models and 
the User model. 
They should each have a name that ends with Type because 
each one represents a GraphQL type.
Resolve a query by taking the information supplied in the 
query and returning the appropriate Django queryset in 
response.
The method for each resolver must start with resolve_, and 
the rest of the name should match the corresponding attribute.
"""
import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from blog import models

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Query(graphene.ObjectType):
    """
    Query class for bringing together all the type classes we have created
    until now.
    Contain attributes and methods to indicate how your models can be queried.
    
    Attibutes:
    all_posts: graphene.List: attribute that will return multiple items.
    author_by_username: grahene.Field: attribute that will return a single item.
    post_by_slug: graphene.Field
    posts_by_author: graphene.List
    posts_by_tag: graphene.List

    For each of the attributes, you also create a method to 
    resolve the query:
    resolve_all_posts(): method: receive all the posts.
    resolve_author_by_username(): method: get an author with a given username.
    resolve_post_by_slug(): method: get a post with a give slug.
    resolve_posts_by_author(): method: receive all posts by a given author.
    resolve_posts_by_tag(): method: receive all posts with a given tag.
    """
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        """
        Receive all the posts.
        """
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        """
        Get an author with a given username.
        """
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )
        
    def resolve_post_by_slug(root, info, slug):
        """
        Get a post with a given slug.
        """
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        """
        Receive all posts by a given author.
        """
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )
    
    def resolve_posts_by_tag(root, info, tag):
        """
        Receive all posts with a given tag.
        """
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )


# Schema variable that wraps your Query class in graphene.Schema to tie it all together
# This variable matches the "blog.schema.schema" value from settings.py file
schema = graphene.Schema(query=Query)