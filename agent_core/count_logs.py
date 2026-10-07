
import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("집계 시작")

with open("sample_logs.csv", "r", encoding="utf-8") as f:
    tot_cnt = 0
    for line in f:
        tot_cnt = tot_cnt + 1

logging.info(f"집계 완료 {tot_cnt}건")
