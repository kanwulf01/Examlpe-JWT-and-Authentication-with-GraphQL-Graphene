import graphene
from graphene_django.types import DjangoObjectType
from vote_link.models import Vote, Link, Link2, Vote2
from django.contrib.auth import get_user_model


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Link2Type(DjangoObjectType):
    class Meta:
        model = Link2

class Vote2Type(DjangoObjectType):
    class Meta:
        model = Vote2

class Query(graphene.ObjectType):
    links = graphene.List(Link2Type)
    votes = graphene.List(Vote2Type)
    users = graphene.List(UserType)
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

    def resolve_links(self, info, **kwargs):
        
        return Link2.objects.all()

    def resolve_votes(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        else:
            return Vote2.objects.all()

    


    