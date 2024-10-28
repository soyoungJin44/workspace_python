import os           #os모듈을 사용해서 환경변수에 접근
from pathlib import Path
from openai import OpenAI
from pathlib import Path

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)


#system 프롬프트
prompt_txt = """
                #context
                해당 주제에 맞는 시를 받아보고싶어.
                최대 5줄의 시로 받고싶어.

                #persona
                너는 시인이야.

                #format
                평시조로 표현해줘

                #tone
                재미있는 톤으로 작성해줘
            """

#메세지
message_history = [
    {"role":"system", "content": prompt_txt},
]


#사용자로부터 질문 입력받기
question = input("***** 주제를 입력해주세요 *****\n\n주제: ")

message_history.append({"role": "user", "content": question})

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages= message_history,
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
print(f"{response.choices[0].message.content}")


#음성 변환

speech_file_path = Path(__file__).parent / "poem.mp3"
response = client.audio.speech.create(
model="tts-1",
voice="alloy",
input={response.choices[0].message.content}
)

response.stream_to_file(speech_file_path)











