from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBr1RHVhIjAdsBqUYoy4LLWKckOIKlqucY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

response = client.chat.completions.create(
    model="models/gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain Cypress testing simply."}
    ],
)

print(response.choices[0].message.content)