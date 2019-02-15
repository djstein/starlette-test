import uvicorn
from databases import Database
from starlette.applications import Starlette
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from example.database import check_database_created
from example.routes import router


DEBUG = True  # TODO: Switch to environment variable!

BASE_SETTINGS = {
    "HOST": "0.0.0.0",
    "PORT": 8000,
    "DEBUG": DEBUG,
    "DATABASE_URL": "postgresql://localhost/starlette",
}

PRODUCTION_SETTINGS = {
    **BASE_SETTINGS,
    "DEBUG": False,
    "MIDDLEWARE": [
        [TrustedHostMiddleware, {"allowed_hosts": ["example.com", "*.example.com"]}],
        HTTPSRedirectMiddleware,
    ],
}

SETTINGS = BASE_SETTINGS if DEBUG else PRODUCTION_SETTINGS


def apply_middleware(app):
    if not SETTINGS.get("MIDDLEWARE"):
        return
    for middleware in SETTINGS.get("MIDDLEWARE"):
        if type(middleware) is list:
            app.add_middleware(middleware[0], **middleware[1])
        else:
            app.add_middleware(middleware)


check_database_created()
database = Database(SETTINGS.get("DATABASE_URL"))
app = Starlette()
app.mount("", router)
app.debug = SETTINGS.get("DEBUG")
apply_middleware(app)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host=SETTINGS.get("HOST"), port=SETTINGS.get("PORT"))

