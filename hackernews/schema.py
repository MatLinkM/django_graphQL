import graphene
import links.schema


class Query(links.schema.Query, graphene.ObjectType):
    pass


class Mutation(links.schema.Mutation, graphene.ObjectType):
    pass

import graphql_jwt
import links.schema
import users.schema

#ativando a consulta na classe principal
class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


class Mutation(links.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)


