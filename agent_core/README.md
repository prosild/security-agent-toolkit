# agent_core

보안 에이전트 구현을 위한 Python 실습 자료. 로그 파싱과 탐지 규칙부터 API 연동, LLM 요약, 보고서 생성과 알림까지 단계별로 구성되어 있습니다.

## 실습 순서

날짜가 붙은 `.ipynb` 파일을 순서대로 확인합니다. `am`은 오전, `pm`은 오후 실습입니다.

| 날짜 | 주요 내용 |
| --- | --- |
| 9/22~23 | Python 자료구조, 조건·반복, 함수, 파일·CSV 처리 |
| 9/28 | 예외 처리, 로깅, 중첩 자료구조와 JSON 정규화 |
| 9/29 | 정규표현식, 탐지 규칙, HTTP와 인증 |
| 9/30 | requests 기반 API 클라이언트와 실패 처리 |
| 10/2 | 웹훅, CLI, 주기 실행과 중복 처리 방지 |
| 10/6 | LLM 프롬프트, 응답 파싱과 도구 호출 |
| 10/7 | 경보 묶음 요약, 위험도 정렬과 보고서 생성 |
| 10/8 | 설정 분리, 알림·파이프라인 통합, 테스트와 디버깅 |

학습 기록은 [docs](../docs/), 1과목 회고는 [day08_retrospective.md](../docs/day08_retrospective.md)에 있습니다.

## 주요 파일

| 파일 | 역할 |
| --- | --- |
| [log_parser.py](log_parser.py), [normalize_logs.py](normalize_logs.py) | 로그 파싱과 공통 구조로 정규화 |
| [api_client.py](api_client.py) | 외부 API 조회 실습 |
| [tool_router.py](tool_router.py) | 도구 이름에 따른 함수 실행 |
| [llm_client.py](llm_client.py) | Gemini API 호출과 JSON 응답 파싱 |
| [event_summarizer.py](event_summarizer.py) | 경보 묶음 요약과 위험도순 정렬 |
| [report_generator.py](report_generator.py) | 건수 집계, 총평과 Markdown 보고서 생성 |
| [notifier.py](notifier.py), [alert_server.py](alert_server.py) | 설정 검사, 승인 필요 여부 판단, 웹훅 송수신 |
| [pipeline.py](pipeline.py) | 경보 입력부터 보고서 저장·알림까지 연결 |
| [test_agent_core.py](test_agent_core.py) | 보고서 형식·승인 판단·JSON 파싱 테스트 9건 |

## 실행 준비

수업에서 사용하는 Python 가상환경을 활성화하고, 저장소 루트에서 실행합니다.

```sh
cd agent_core
python -m pip install requests flask
```

주기 실행 실습인 `scheduler_job.py`에는 `schedule` 패키지도 필요합니다. 노트북은 VS Code 또는 Jupyter에서 같은 가상환경을 커널로 선택합니다.

`agent_core/.env`에 다음 형식으로 Gemini API 키를 저장합니다. 기존 파일이 있다면 필요한 항목만 추가합니다.

```dotenv
GEMINI_API_KEY=발급받은_API_키
```

현재 `.env.example`의 `API_KEY`는 이전 API 실습용 이름입니다. LLM 코드에서는 `GEMINI_API_KEY`를 읽습니다. `.env`는 Git 추적 제외 대상입니다.

[config.json](config.json)에서 실행 설정을 확인합니다.

| 키 | 역할 |
| --- | --- |
| `model` | 호출할 모델 이름 |
| `approve_severity` | 사람 확인이 필요한 최소 위험도: `low`, `medium`, `high` |
| `webhook_url` | 알림 주소. 실습 서버 기본값은 `http://127.0.0.1:5001/alert` |
| `report_folder` | 보고서 폴더 실습용 설정. 현재 파이프라인의 저장 경로에는 미반영 |

## 보고서 파이프라인

두 터미널 모두 `agent_core` 폴더에서 같은 가상환경으로 실행합니다.

터미널 1 — 알림 서버:

```sh
python alert_server.py
```

터미널 2 — 보고서 생성:

```sh
python pipeline.py
```

처리 흐름: 경보 읽기 → LLM 요약 → 위험도 정렬 → 총평·보고서 생성 → 저장 → 사람 확인 대상 집계 → 웹훅 알림

- 현재 입력은 `events_1008.json`으로 고정되어 있습니다.
- 보고서는 실행 날짜 기준 `daily_report_YYYYMMDD.md`로 현재 폴더에 저장됩니다. 같은 날짜에 다시 실행하면 덮어씁니다.
- 실제 LLM API를 호출하므로 키와 네트워크 연결이 필요하며, 요약과 위험도 판단은 실행마다 달라질 수 있습니다.
- 알림 서버 연결이 실패해도 먼저 저장한 보고서는 유지됩니다. 현재 알림 함수는 HTTP 오류 상태를 별도로 검사하지 않습니다.

## 테스트

```sh
python test_agent_core.py
```

LLM이나 알림 서버를 호출하지 않고 함수의 입력과 반환값을 검사합니다. 모두 통과하면 `[테스트 통과] 9건 모두`가 출력됩니다.

노트북의 `%%writefile` 셀은 같은 이름의 Python 파일을 덮어씁니다. 수정한 코드가 있다면 준비 셀을 다시 실행하기 전에 내용을 확인합니다.
