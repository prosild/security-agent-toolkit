import re

ip_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
mac_pattern = r"^([0-9A-Fa-f]{2}-){5}([0-9A-Fa-f]{2})$"

def kind(address):                                # 주소의 모양을 보고 종류를 리턴하는 함수
    # 1. address 를 "." 로 나눈 조각이 4개이면 "IP" 를 return 하세요
    if re.match(ip_pattern, a):
            return "IP"
    # 2. address 를 "-" 로 나눈 조각이 6개이면 "MAC" 을 return 하세요
    elif re.match(mac_pattern, a):
        return "MAC"
    # 3. 둘 다 아니면 "모름" 을 return 하세요
    else:
        return "모름"


# ── 미리 채워 둔 줄입니다. 고치지 않습니다 ──
for a in ["192.168.0.15", "a8-5e-45-01-2b-3c", "ff-ff-ff-ff-ff-ff", "192.168.0"]:
    print(kind(a), a)                             # 종류와 주소를 한 줄에
# ── 여기까지 ──