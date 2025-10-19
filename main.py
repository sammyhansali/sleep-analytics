import logging

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Hello from sleep-analytics!")


if __name__ == "__main__":
    main()
