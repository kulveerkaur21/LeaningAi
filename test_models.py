from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBr1RHVhIjAdsBqUYoy4LLWKckOIKlqucY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

try:
    models = client.models.list()
    print("Available models:")
    for model in models.data:
        print(f"- {model.id}")
except Exception as e:
    print(f"Error: {e}")
