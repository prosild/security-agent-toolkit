import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("파서 시작: sample_logs_broken.csv")

logs = []
with open("sample_logs_broken.csv", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        try:
            logs.append(parts[3])
        except IndexError:
            logging.warning(f"깨진 줄 건너뜀: {line.strip()}")

logging.info(f"정상 로그 {len(logs)}건 처리 완료")
print(f"정상 로그 {len(logs)}건")
