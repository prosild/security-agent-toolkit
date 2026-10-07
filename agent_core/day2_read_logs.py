
count = 0
with open("sample_logs.csv", encoding="utf-8") as f:
    for line in f:
        # ← 문제 6-4의 답을 붙이세요 (FAIL 이 든 줄만 출력)
        # ← 그 아래에 count = count + 1
        if "FAIL" in line:
            print(line)
            count = count + 1

print(f"실패 {count}줄")
