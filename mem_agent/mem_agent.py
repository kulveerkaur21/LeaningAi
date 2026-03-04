from mem0 import Memory
import os
import json
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
config = {
    "version" : "v1.1",
    "embedder" : {
        "provider" : "openai",
        "config" : {
            "api_key" : OPEN_API_KEY ,
            "model" : "text-embedding-3-small"
        }
    },
    "llm" : {
        "provider" : "openai",
        "config" : {
            "api_key" : OPEN_API_KEY ,
            "model" : "gpt-4.1"
        }
    },
    "vector_store" : {
        "provider" : "qdrant",
        "config" : {
            "host" : "localhost",
            "port" : 6333,
            "collection_name" : "mem-agent"
        }
    }
}

mem_client = Memory.from_config(config)

while True:
    user_query = input(">")

    serach_memory = mem_client.search(query=user_query,user_id="1")

    print("Search Memory", serach_memory)


    memories = [
    f"ID: {memory.get('user_id', '')}\nMemory: {memory.get('memory', '')}" for memory in serach_memory.get("results", [])
    ]


    System_Prompt = f"""You are a helpful assistant. Use the following context to answer the question.
    {json.dumps(memories)}
    """

    print("found memories", len(memories))

    response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": System_Prompt},
        {"role": "user", "content": user_query}
    ]
)
    ai_response = response.choices[0].message.content

    print("AI" , ai_response)

    mem_client.add(
    user_id = "1",
    messages=[
        {"role": "user", "content": user_query},
        { "role" : "assistant","content": ai_response}
    ]
)

    print("Memory has been saved")