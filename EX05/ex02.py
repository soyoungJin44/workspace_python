'''
1. 최소버전 + 토큰값
2. 이전내용 기억하기

'''

import os           #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

#openai_key = "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"

client = OpenAI(api_key = openai_api_key)

#system 프롬프트
prompt_txt = """
                #context
                100글자 이내로 답해줘
            """
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role":"system","content":prompt_txt},
        {"role":"user","content":"대한민국의 수도는?"},
        {"role":"assistant","content":"대한민국의 수도는 서울입니다. 혹시 더 궁금한 것이 있으시면 또 말씀해주세요"}
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "text"
    }
)

"""응답에서 원하는 답의값만 출력하기"""
print(response.choices[0])

#토큰수 확인
#q_token = response.usage.prompt_tokens      #질문토큰수
#a_token = response.usage.completion_tokens    #응답토큰수
#response.usage.prompt_tokens  #전체토큰수
#print(f"질문:{q_token}+ 응답:{a_token}+전체:{q_token+a_token}")


