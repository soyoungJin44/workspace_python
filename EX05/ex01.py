'''
1. 최소버전 + 토큰값

'''

import os           #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key = openai_api_key)


response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role":"system","content":"너는 신지연 31살, 여자이고 굉장히 해맑은 아이야. 사람들이 너를 미친사람이라고 불러. "},
        {"role":"user","content":"너에대해 웃기고 놀리는것처럼 30글자 이내로 설명해봐"}
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
print(response.choices[0].message.content)

#토큰수 확인
q_token = response.usage.prompt_tokens      #질문토큰수
a_token = response.usage.completion_tokens    #응답토큰수
response.usage.prompt_tokens  #전체토큰수
print(f"질문:{q_token}+ 응답:{a_token}+전체:{q_token+a_token}")


