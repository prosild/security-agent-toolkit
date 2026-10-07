
import logging
from collections import Counter

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

FILE_NAME = "sample_logs_broken2.csv"

logging.info("파서 시작: %s", FILE_NAME)

def parse_line(line):
    temp_arr = line.strip().split(",")
    int(temp_arr[0].split(":")[0])
    return {"time": temp_arr[0], "user": temp_arr[1], "event": temp_arr[2], "ip": temp_arr[3]}

try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        log_list = []
        for line in f:
            try:
                log_list.append(parse_line(line))
            except IndexError:
                logging.warning("칸이 모자란 줄: %s", line)
            except ValueError:
                logging.warning("시각이 깨진 줄: %s", line)
except FileNotFoundError:
    logging.error("로그 파일을 찾을 수 없음")
    break

logging.info(f"정상 로그 {len(log_list)}건 처리 완료")

failed_user = []

for log in log_list:
    if log["event"] == "LOGIN_FAIL":
        failed_user.append(log["user"])

fail_cnt = Counter(failed_user)

for k, v in fail_cnt.items():
    if v >= 3:
        print(k)
