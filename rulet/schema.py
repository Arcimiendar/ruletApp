import ruletApp.schema
import graphene


class Query(ruletApp.schema.schema.Query, graphene.ObjectType):
    pass


class Mutation(ruletApp.schema.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
