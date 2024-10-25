from openai import OpenAI
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

response = client.images.generate(
    model="dall-e-3",
    prompt="",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)