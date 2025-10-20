import json
import pathlib
import logging.config
from urllib.parse import urlencode
import requests

logger = logging.getLogger("sleep-analytics")

def logging_setup():
    logging_config = pathlib.Path("logging_config/basic.json")

    with open(logging_config, "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    
def main():
    logging_setup()

    logger.info("Hello from sleep-analytics!")

    # try running the token_request.py script for trying to setup api access


if __name__ == "__main__":
    main()
