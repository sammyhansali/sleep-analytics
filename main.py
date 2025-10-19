import json
import pathlib
import logging.config

logger = logging.getLogger("sleep-analytics")

def logging_setup():
    logging_config = pathlib.Path("logging_config/basic.json")

    with open(logging_config, "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    
def main():
    logging_setup()

    logger.info("Hello from sleep-analytics!")


if __name__ == "__main__":
    main()
