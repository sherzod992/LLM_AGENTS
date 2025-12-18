# LLM 에이전트 프로젝트

## LLM이란?

- **L**arge: 대형
- **L**anguage: 언어  
- **M**odel: 모델

대규모 언어 모델을 의미합니다.

## 프로젝트 개요

일반적인 가장 간단한 LLM 에이전트 구현 예제입니다. 

**LLM 에이전트의 핵심 역할**: 각 에이전트 애플리케이션의 "사고"를 담당합니다.

## LLM 에이전트의 기본 정의

1. **이름 (Name)** - 필수
2. **모델 (Model)** - 필수
3. **설명 (Description)** - 권장
4. **지침 (Instruction)** - 권장 (핵심 기능)

## 에이전트 기능

이 에이전트는 다음과 같은 대화 흐름을 가집니다:

1. 사용자가 인사말을 입력
2. 에이전트가 나이를 물어봄
3. 사용자가 나이를 입력
4. 에이전트가 나이에 맞는 적극적인 격려 메시지를 제공

## 프로젝트 구조

```
LLM_AGENT/
├── agents/
│   ├── __init__.py
│   └── agent.py          # 메인 에이전트 구현
├── .env                  # API 키 저장 (git에 커밋하지 않음)
└── README.md
```

## 설치 및 실행

### 1. 가상환경 생성 (선택사항)

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### 2. 필요한 패키지 설치 (실제 LLM 사용 시)

```bash
pip install google-generativeai python-dotenv
```

### 3. API 키 설정 (선택사항)

`.env` 파일에 Google API 키를 설정하세요:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

**참고**: 현재는 API 키 없이도 동작하는 간단한 규칙 기반 버전으로 구현되어 있습니다.  
실제 LLM을 사용하려면 `agent.py` 파일의 주석 처리된 코드를 해제하세요.

### 4. 에이전트 실행

```bash
python agents/agent.py
```

또는 Python 모듈로 실행:

```bash
python -m agents.agent
```

## 사용 예시

```
=== 격려 에이전트에 오신 것을 환영합니다! ===
종료하려면 'quit', 'exit', '종료' 중 하나를 입력하세요.

사용자: 안녕하세요
에이전트: 안녕하세요! 반갑습니다! 혹시 나이를 알려주실 수 있나요? 나이를 알려주시면 그에 맞는 격려 메시지를 드릴게요!

사용자: 25살이에요
에이전트: 25살, 인생의 황금기입니다! 지금이야말로 도전하고 성장할 수 있는 최고의 시기예요. 두려워하지 말고 자신의 길을 개척해 나가세요. 당신 안에 있는 무한한 잠재력을 믿으세요! 화이팅! 💪🔥
```

## 참고사항

- 현재 구현은 규칙 기반 방식으로 동작하며, API 키 없이도 테스트할 수 있습니다.
- 실제 Google Generative AI를 사용하려면 `agent.py`의 주석 처리된 코드를 활성화하세요.
- `.env` 파일은 절대 git에 커밋하지 마세요 (보안상 중요).
