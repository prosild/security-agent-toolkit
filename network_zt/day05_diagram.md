# day05 경보 판단

## 이상한 줄
- 줄 번호(여러 개면 모두): 2번, 3번
- 이유: 구성도에서 DB 는 INSIDE 에 있어 인터넷에서 바로 닿으면 안됨
인터넷의 192.0.2.7 이 DB 3306에 permit
1번은 인터넷에서 WEB 443 으로 가는 길이라 구성도상 허용된 길

## 고친 구성도
```
INTERNET ──── FW ──┬── DMZ    : WEB (443 open)
                   └── INSIDE : DB  (3306 from WEB only)
```