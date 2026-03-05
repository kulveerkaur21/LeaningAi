from openai import OpenAI
from mem0 import Memory
import os
import json
from dotenv import load_dotenv
load_dotenv()

# Neo4j connection test - credentials removed for security
# uri = "neo4j+s://your-neo4j-url"
# driver = GraphDatabase.driver(uri, auth=("username", "password"))
# with driver.session() as session:
#     print(session.run("RETURN 1").single())
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
        "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "neo4j+s://your-neo4j-url",
            "username": "your-username",
            "password": "your-password",
            "database": "your-database"
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


client = OpenAI(api_key=OPEN_API_KEY)
client.models.list()
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