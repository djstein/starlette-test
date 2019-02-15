import uvicorn
from starlette.applications import Starlette
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from example.database import check_database_created
from example.routes import router

DEBUG = True  # TODO: Switch to environment variable!

BASE_CONFIG = {"HOST": "0.0.0.0", "PORT": 8000, "DEBUG": DEBUG}

PRODUCTION_CONFIG = {
    **BASE_CONFIG,
    "DEBUG": False,
    "MIDDLEWARE": [
        [TrustedHostMiddleware, {"allowed_hosts": ["example.com", "*.example.com"]}],
        HTTPSRedirectMiddleware,
    ],
}

ACTIVE_CONFIG = BASE_CONFIG if DEBUG else PRODUCTION_CONFIG


def apply_middleware(app):
    if not ACTIVE_CONFIG.get("MIDDLEWARE"):
        return
    for middleware in ACTIVE_CONFIG.get("MIDDLEWARE"):
        if type(middleware) is list:
            app.add_middleware(middleware[0], **middleware[1])
        else:
            app.add_middleware(middleware)


check_database_created()
app = Starlette()
app.mount("", router)
app.debug = ACTIVE_CONFIG.get("DEBUG")
apply_middleware(app)


if __name__ == "__main__":
    uvicorn.run(app, host=ACTIVE_CONFIG.get("HOST"), port=ACTIVE_CONFIG.get("PORT"))

