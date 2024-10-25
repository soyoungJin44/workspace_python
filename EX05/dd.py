import os
from openai import OpenAI

# API 키 설정 
openai_key= os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=openai_key)

def analyze_situation(situation):
    """상황을 분석하고 응답을 반환하는 함수"""
    
    analysis_prompt = f"""
    다음 상황에 대해 분석해주세요. 각 항목을 100점 만점으로 평가하고, 
    간단한 이유도 설명해주세요:

    상황: {situation}

    다음 형식으로 답변해주세요:
    합리성: (점수)점 - (이유)
    감정적측면: (점수)점 - (이유)
    윤리성: (점수)점 - (이유)
    
    종합의견: (전체적인 분석)
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": analysis_prompt}],
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content

print("=== 상황 분석 프로그램 ===")
print("상황을 입력하면 분석 결과를 알려드립니다.")
print("종료하려면 '/q'를 입력하세요.")
print("-" * 40)

while True:
    situation = input("\n분석할 상황을 설명해주세요: ")
    
    if situation.lower() == '/q':
        print("\n프로그램을 종료합니다.")
        break
    
    try:
        result = analyze_situation(situation)
        print("\n[분석 결과]")
        print(result)
        print("-" * 40)
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")