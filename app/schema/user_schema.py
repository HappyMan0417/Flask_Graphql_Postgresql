import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models.user_model import ExampleModel
from app.models import db_session

class ExampleModelObject(SQLAlchemyObjectType):
    class Meta:
        model = ExampleModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_examples = SQLAlchemyConnectionField(ExampleModelObject)


class CreateExample(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    example = graphene.Field(lambda: ExampleModelObject)

    def mutate(self, info, first_name, last_name, email):
        example = ExampleModel(first_name=first_name, last_name=last_name, email=email)
        db_session.add(example)
        db_session.commit()
        return CreateExample(example=example)

class UpdateExample(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()

    example = graphene.Field(lambda: ExampleModelObject)

    def mutate(self, info, id, name):
        example = db_session.query(ExampleModel).filter_by(id=id).first()
        if example is None:
            return None
        else:
            example.name = name
            db_session.commit()
            return UpdateExample(example=example)

class DeleteExample(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        example = db_session.query(ExampleModel).filter_by(id=id).first()
        db_session.delete(example)
        db_session.commit()
        return DeleteExample(ok=True)

class Mutation(graphene.ObjectType):
    create_example = CreateExample.Field()