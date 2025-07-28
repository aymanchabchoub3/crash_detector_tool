from loguru import logger

logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="1 day",
    format="{time} | {level} | {message}",
    serialize=True,
)


def main():
    logger.info("Crash Detection Tool initialized")


if __name__ == "__main__":
    main()
