import re
import json

PATTERN = r"(?P<time>(?:\d{2}:){2}\d{2}) (?P<level>(INFO|WARN|ERROR)) \w+ login for (?P<user>[\w.]+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"

def parse_raw_logs(line):
    m = re.search(PATTERN, line)
    if m:
        return m.groupdict()
    else:
        return None

# rows와 unmatched를 만들고 파일 두 개로 저장하는 코드를 이어서 작성합니다.
rows = []
unmatched = []

with open("raw_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        row = parse_raw_logs(line)

        if row:
            rows.append(row)
        else:
            unmatched.append(line.strip())

with open("normalized_logs.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

with open("unmatched_logs.txt", "w", encoding="utf-8") as f:
    f.writelines(unmatched)

print(f"정규화 {len(rows)}건")
print(f"안 맞음 {len(unmatched)}건")
