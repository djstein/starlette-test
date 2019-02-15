from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists


def check_database_created(database_uri="postgres://localhost/starlette"):
    engine = create_engine(database_uri)
    if not database_exists(engine.url):
        print(f"Database {database_uri} not found, creating...")
        create_database(engine.url)
    print(f"Database {database_uri} found: {database_exists(engine.url)}")
