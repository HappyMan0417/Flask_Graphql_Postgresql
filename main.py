from flask import Flask
from app.models import db_session
from app.schema import schema
from flask_graphql import GraphQLView
from app.models.database import init_database

app = Flask(__name__)
app.debug = True

database_uri = 'postgresql://postgres:postgres@localhost/test'
init_database(database_uri)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()