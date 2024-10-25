from openai import OpenAI
import os
import uuid
import requests

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

response = client.images.generate(
    model="dall-e-3",
    prompt="cat, black, korea",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)

##############################################################

#다운로드 받을 경로
download_path = "C:\\javaStudy\\upload_python"

#파일 이름 만들어주기
file_name = str(uuid.uuid4())+".png"

#이미지 다운로드
response = requests.get(image_url)

#유효성 검사 ( 200:성공 ,400:실패 )
if response.status_code == 200:
    file_path = os.path.join(download_path, file_name)
    with open(file_path, "wb") as file:
        file.write(response.content)

    print("다운로드 끄읏")
else:
    print("url 오류")