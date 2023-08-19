import logging

from inferno3_database import start_web_server

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def web_server() -> None:
    start_web_server()
