import motor.motor_asyncio

from inferno3_database import config


def create_indexes(db):
    db.items.create_index("name", unique=True)
    db.items.create_index([("price", "text")])


def start_db():
    database_url = config["db"]["url"]
    database_name = config["db"]["database"]

    client = motor.motor_asyncio.AsyncIOMotorClient(
        database_url, tls=True, tlsAllowInvalidCertificates=True
    )
    create_indexes(client[database_name])
    return client, client[database_name]
