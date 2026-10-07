import logging

logging.basicConfig(
    filename="short_format.log",
    level=logging.WARNING,
    format="%(asctime)s %(message)s",
    encoding="utf-8",
)

logging.warning("주의")
