import graphene
from starlette.graphql import GraphQLApp
from starlette.routing import Mount, Route, Router
from example.views import Homepage
from example.queries import QueryAPI


router = Router(
    [
        Route("/", endpoint=Homepage, methods=["GET"]),
        Route(
            "/graph/v1/", endpoint=GraphQLApp(schema=graphene.Schema(query=QueryAPI))
        ),
    ]
)
