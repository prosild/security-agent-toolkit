
import logging

logging.basicConfig(
    filename="only_error.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("시작")
logging.warning("주의")
logging.error("오류")
