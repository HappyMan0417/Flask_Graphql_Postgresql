from .user_schema import Query, Mutation

import graphene

schema = graphene.Schema(query=Query, mutation=Mutation)