from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Llama-2 instruction format
instruction_prompt = """[INST] <<SYS>>
You are a helpful AI assistant that explains concepts clearly.
<</SYS>>

What is artificial intelligence? [/INST]"""

response = client.chat.completions.create(
    model="models/gemini-2.5-flash",
    messages=[
        {"role": "user", "content": instruction_prompt}
    ],
)

print(response.choices[0].message.content)
