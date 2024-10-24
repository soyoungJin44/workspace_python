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
7. system 사이트정보 추가



'''

import os           #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")



client = OpenAI(api_key = openai_api_key)

#system 프롬프트
prompt_txt = """
                #context
                -당신은 100글자 이내로 답해주세요.
                -당신은 고객의 질문에 최선을 다해 친절하게 대답합니다.
                -질문에 해당하는 내용을 요약해서 대답하며 url정보가 있는경우 링크정보도 제공합니다.
                -질문에 대한 정보가 없는 경우 아래의 메세지를 출력합니다.
                ----
                죄송합니다. 고객센터로 문의 바랍니다.
                02-2222-2222
                ----
                #쇼핑몰 정보
                ----
                영업시간: 오전9시30분 부터 오후 6시 10분까지 영업
                위치: 강남역 10번 출구
                회원탈퇴방법: 불가
                ----

                #persona
                당신은 쇼핑몰의 상담사 입니다.
                항상 고객을 공손하게 맞이하며 고객을 최우선으로 생각합니다.

                #tone
                공손하고 친절하게 대답해줘

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

        if len(message_history) == 11:
            print("질문 횟수가 끝났습니다.")
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

