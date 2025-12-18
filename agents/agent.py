"""
LLM 에이전트 구현

사용자와 대화하며 나이를 물어보고, 나이에 맞는 격려 메시지를 제공하는 에이전트입니다.
"""

import os
from typing import Optional

# API 키 관련 설정
# 실제 사용 시 아래 주석을 해제하고 .env 파일에서 API 키를 로드하세요
# from dotenv import load_dotenv
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Google Generative AI 사용 시 주석 해제
# import google.generativeai as genai
# genai.configure(api_key=GOOGLE_API_KEY)


class LLMAgent:
    """
    LLM 에이전트 클래스
    
    기능:
    1. 사용자의 인사말을 받으면 나이를 물어봄
    2. 나이를 입력받으면 나이에 맞는 적극적인 격려 메시지를 제공
    """
    
    def __init__(self):
        """에이전트 초기화"""
        self.name = "격려 에이전트"
        self.model_name = "gemini-pro"  # 실제 사용 시 모델명
        self.description = "나이에 맞는 적극적인 격려 메시지를 제공하는 에이전트"
        self.instruction = """
        당신은 사용자를 격려하는 친근한 에이전트입니다.
        사용자의 나이를 물어보고, 나이에 맞는 적극적이고 힘을 줄 수 있는 메시지를 제공하세요.
        """
        self.conversation_state = "greeting"  # greeting, asking_age, completed
        self.user_age: Optional[int] = None
        
        # 실제 LLM 모델 사용 시 주석 해제
        # self.model = genai.GenerativeModel(self.model_name)
    
    def _get_greeting_response(self) -> str:
        """인사말에 대한 응답 반환"""
        self.conversation_state = "asking_age"
        return "안녕하세요! 반갑습니다! 혹시 나이를 알려주실 수 있나요? 나이를 알려주시면 그에 맞는 격려 메시지를 드릴게요!"
    
    def _get_encouragement_by_age(self, age: int) -> str:
        """나이에 맞는 격려 메시지 생성"""
        if age < 10:
            return f"와! {age}살이면 정말 어린 나이네요! 무엇이든 배우고 시도할 수 있는 멋진 나이예요! 새로운 것을 배우고 도전하는 용기를 가지세요. 당신은 놀라운 가능성을 가지고 있습니다! 💪🌟"
        elif age < 20:
            return f"{age}살, 청소년 시기는 인생의 중요한 시기입니다! 지금 당신이 하는 모든 노력과 선택이 미래를 만들어갑니다. 꿈을 향해 당당하게 나아가세요. 어려움이 있어도 포기하지 마세요! 화이팅! 🚀✨"
        elif age < 30:
            return f"{age}살, 인생의 황금기입니다! 지금이야말로 도전하고 성장할 수 있는 최고의 시기예요. 두려워하지 말고 자신의 길을 개척해 나가세요. 당신 안에 있는 무한한 잠재력을 믿으세요! 화이팅! 💪🔥"
        elif age < 40:
            return f"{age}살, 경험과 지혜가 쌓이는 시기입니다! 지금까지의 경험을 바탕으로 더 큰 도전에 나설 수 있어요. 새로운 시작을 두려워하지 마세요. 나이보다 중요한 것은 열정과 도전 정신입니다! 계속해서 성장하세요! 🌟💪"
        elif age < 50:
            return f"{age}살, 인생에서 가장 성숙하고 안정적인 시기입니다! 지금까지의 경험은 당신의 자산입니다. 새로운 목표를 세우고 달성해 나가세요. 나이는 숫자일 뿐, 중요한 것은 지금 이 순간을 어떻게 살아가느냐입니다! 화이팅! 🚀✨"
        else:
            return f"{age}살, 인생의 모든 경험이 빛나는 시기입니다! 나이는 당신을 제한하지 않습니다. 지금도 충분히 새롭게 시작할 수 있어요. 지혜와 경험으로 새로운 도전을 해나가세요. 당신의 인생은 아직 멋진 이야기가 계속됩니다! 💪🌟"
    
    def _parse_age(self, text: str) -> Optional[int]:
        """텍스트에서 나이 추출"""
        import re
        # 숫자 찾기
        numbers = re.findall(r'\d+', text)
        if numbers:
            age = int(numbers[0])
            # 합리적인 나이 범위 체크 (0-120)
            if 0 <= age <= 120:
                return age
        return None
    
    def process_message(self, user_input: str) -> str:
        """
        사용자 메시지를 처리하고 응답 반환
        
        Args:
            user_input: 사용자가 입력한 메시지
            
        Returns:
            에이전트의 응답 메시지
        """
        user_input_lower = user_input.lower().strip()
        
        # 인사말 체크 (초기 상태일 때)
        if self.conversation_state == "greeting":
            greeting_keywords = ['안녕', 'hello', 'hi', '안녕하세요', '반가워', '하이']
            if any(keyword in user_input_lower for keyword in greeting_keywords):
                return self._get_greeting_response()
            else:
                # 인사말이 아니어도 나이 물어보기
                self.conversation_state = "asking_age"
                return "안녕하세요! 혹시 나이를 알려주실 수 있나요?"
        
        # 나이 물어보는 상태
        elif self.conversation_state == "asking_age":
            age = self._parse_age(user_input)
            if age is not None:
                self.user_age = age
                self.conversation_state = "completed"
                return self._get_encouragement_by_age(age)
            else:
                return "숫자로 나이를 알려주세요! 예: 25살, 30, 스물다섯 등"
        
        # 대화 완료 상태 (추가 대화 가능)
        else:
            # 다시 나이를 물어보거나 새로운 대화 시작
            if '나이' in user_input_lower or '몇 살' in user_input_lower:
                self.conversation_state = "asking_age"
                return "나이를 알려주세요!"
            else:
                return "언제든지 필요하시면 말씀해주세요! 추가로 도와드릴 일이 있나요?"
    
    def reset(self):
        """대화 상태 초기화"""
        self.conversation_state = "greeting"
        self.user_age = None
    
    def chat(self):
        """
        대화형 인터페이스로 에이전트 실행
        
        실제 LLM 사용 시 주석 해제하고 구현:
        response = self.model.generate_content(prompt)
        return response.text
        """
        print(f"=== {self.name}에 오신 것을 환영합니다! ===")
        print("종료하려면 'quit', 'exit', '종료' 중 하나를 입력하세요.\n")
        
        while True:
            user_input = input("사용자: ")
            
            if user_input.lower().strip() in ['quit', 'exit', '종료']:
                print("\n에이전트를 종료합니다. 좋은 하루 되세요! 👋")
                break
            
            if not user_input.strip():
                continue
            
            response = self.process_message(user_input)
            print(f"에이전트: {response}\n")


if __name__ == "__main__":
    # 에이전트 테스트
    agent = LLMAgent()
    agent.chat()
