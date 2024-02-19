import os

import uvicorn
from pyaml_env import parse_config, BaseConfig


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

config = BaseConfig(parse_config(ROOT_DIR + "/config.yaml"))

print(config)


def start_web_server() -> None:
    uvicorn.run(
        "inferno3_database.application:app",
        host="0.0.0.0",
        port=4000,
        reload=True,
    )


if __name__ == "__main__":
    start_web_server()
