import graphene
from django.contrib.auth import get_user_model
from vote_link.models import Link2, Vote2
from .types import Link2Type, UserType
import graphql_jwt

# ...code
# Change the CreateLink mutation
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    author = graphene.String()
    

    class Arguments:
        url = graphene.String()
        author = graphene.String()

    def mutate(self, info, url, author):

        link = Link2(
            url=url,
            author=author,
            
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            author=link.author,
           
        )


class CreateVote(graphene.Mutation):
    link = graphene.Field(Link2Type)

    class Arguments:
        
        link_id = graphene.Int()
        
    def mutate(self, info,link_id):

        link = Link2.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!')

        Vote2.objects.create(
            
            link=link,
        )

        return CreateVote(link=link)

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_vote = CreateVote.Field()
    create_link = CreateLink.Field()
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


   