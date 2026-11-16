# 5과목 Day 5 최종 회고 (2026-11-16(월))

## 1. 5일 동안 만든 것

엔진이 각 날의 파일을 어디에 쓰는지 한 문장씩 씁니다.

| Day | 날짜 | 엔진과 연결된 파일 | 엔진에서 하는 일 |
|---|---|---|---|
| 1 | 11/9(월), 11/10(화) | `incident.py`, `config/playbook_registry.json` | 탐지된 규칙과 등급에 맞는 플레이북을 탐색하고 실행 절차를 결정함 |
| 2 | 11/11(수) | `account_actions.py`, `ip_actions.py` | VIP 계정과 허용 목록 예외를 반영하여 계정 잠금 및 IP 임시 차단 조치를 실행함 |
| 3 | 11/12(목) | `ticketing.py` | 조치 실행 결과와 알림 상태를 바탕으로 대응 담당자가 확인할 표준 티켓을 생성함 |
| 4 | 11/13(금) | `approval_gate.py` | 조치 대상의 위험 점수를 산출하여 자동 실행, 담당자 승인 필요, 차단 금지로 분기함 |
| 5 | 11/16(월) | `soar_engine.py`, `engine_input.py`, `policy_check.py` | 탐지 결과 스키마 검증부터 플레이북 매칭, 승인 게이트, 조치 실행, 티켓 생성까지 종단간 오케스트레이션을 수행하고 정책 준수 여부를 검증함 |

## 2. 운영하면 깨질 수 있는 곳 3가지

오늘 출력이나 코드에서 근거를 찾아 씁니다.

| 깨질 곳 | 근거(오늘의 파일, 단계) | 막는 방법 |
|---|---|---|
| 상류 시스템의 스키마 변경 | `engine_input.py` 3교시 단계 2 (minsu의 critical 등급과 hana의 grade 키 누락) | 엔진 앞단에서 `find_schema_problem`으로 사전 입력 검증을 수행하고 거절 리스트로 격리함 |
| 개별 알림 처리 중 예외 발생 | `soar_engine.py` 2교시 단계 2 (INC-402의 KeyError: 'grade') | `run_all`의 `try`/`except Exception` 구문으로 오류를 격리하여 후속 알림 처리가 중단되지 않도록 함 |
| 승인 게이트 우회 및 잘못된 조치 실행 | `policy_check.py` 4교시 단계 2 (`gate_off_log.json` 점검 결과 FAIL) | 저장된 조치 요청(`request`)으로 승인 결정을 재수행(`decide_gate`)하고 허용 목록과 VIP 불변 조건을 정기적으로 감사 점검함 |

## 3. 캡스톤 주제와 내 모듈

| 캡스톤 주제 | 쓰는 과목 모듈 |
|---|---|
| 과다권한 자동 회수봇 | `access_control` + `agent_core` |
| 이상행위 자동 차단 에이전트 | `anomaly_detection` + `soar_response` |
| ZT 보안 자세 점검, 스코어링 | `network_zt` + `agent_core` |
| AI 보안 이벤트 분류, 초동대응봇 | `anomaly_detection` + `soar_response` + `agent_core` |

- 내가 고르고 싶은 주제: 이상행위 자동 차단 에이전트
- 캡스톤 첫날 새 코드 없이 바꿔 볼 설정 파일 2개: `config/playbook_registry.json`, `config/approval_policy.json`
- 그대로 가져다 쓸 내 파일 3개: `soar_engine.py`, `approval_gate.py`, `policy_check.py`
