'''
1. 최소버전 + 토큰값
---
2. 이전내용 기억하기
---
3. 사용자가 질문 입력하기
----
4. 화면만들기
---
5. 질문누적
---

'''

import os           #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key = openai_api_key)

#system 프롬프트
prompt_txt = """
                #context
                100글자 이내로 답해줘
            """

message_history = [
    {"role":"system", "content": prompt_txt},
]

#사용자로부터 질문 입력받기
print("*"*50)
print("반갑습니다. 질문을 입력해주세요!")
print("*"*50)

while True:

    question = input("(사용자)")

    if question == "\q":
        print("이용해주셔서 감사합니다!")
        break
    else:
        #질문 추가하기
        message_history.append({"role":"user", "content": question})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=message_history,
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
        # print(response.choices[0].message.content)
        print(f"[쳇_GPT]:{response.choices[0].message.content}")
        message_history.append({"role":"assistant", "content": response.choices[0].message.content})        #받은 답변을 리스트에 쌓기

        #print(message_history)

#토큰수 확인
#q_token = response.usage.prompt_tokens      #질문토큰수
#a_token = response.usage.completion_tokens    #응답토큰수
#response.usage.prompt_tokens  #전체토큰수
#print(f"질문:{q_token}+ 응답:{a_token}+전체:{q_token+a_token}") 

