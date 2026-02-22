# Weather Agent - Main File
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

userquery = input(">")
response = client.chat.completions.create(
    model="models/gemini-2.5-flash",
    messages=[
        {"role": "user", "content": userquery}
    ]
)

print(f"Response: {response.choices[0].message.content}")