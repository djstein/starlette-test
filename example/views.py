from starlette.responses import JSONResponse, PlainTextResponse
from starlette.endpoints import HTTPEndpoint
from starlette.graphql import GraphQLApp


class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")

