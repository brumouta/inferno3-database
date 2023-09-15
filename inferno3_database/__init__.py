import os

import uvicorn
import yaml


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(ROOT_DIR + "/../config.yaml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    print("Successfully loaded the configuration")


def start_web_server() -> None:
    uvicorn.run(
        "inferno3_database.application:app",
        port=4000,
        reload=True,
    )


if __name__ == "__main__":
    start_web_server()
