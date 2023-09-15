import motor.motor_asyncio

from inferno3_database import config


def start_db():
    database_url = config["db"]["url"]
    database_name = config["db"]["database"]

    client = motor.motor_asyncio.AsyncIOMotorClient(database_url,
                                                    tls=True,
                                                    tlsAllowInvalidCertificates=True)

    return client, client[database_name]
