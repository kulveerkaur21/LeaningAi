from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBr1RHVhIjAdsBqUYoy4LLWKckOIKlqucY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

response = client.chat.completions.create(
    model="models/gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "What is Python?"}
    ],
)

print(response.choices[0].message.content)
