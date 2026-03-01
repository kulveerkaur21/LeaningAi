# Weather Agent - Main File
from openai import OpenAI
import requests
import json

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

System_prompt = """ 
You're an expert AI Assistant in resolving user queries related to weather.
You have access to a tool that can provide weather information for a given city.
You should use this tool to answer user queries.

Rules:
- Strictly follow given JSON output format
- Only run one step at a time
- After planning, immediately execute the tool
- Always provide final weather output

Available tools:
- get_weather(city): Returns weather information for a city

Output format:
{"steps": "Start" | "Plan" | "Tools" | "output", "content": "string"}

Example:
{"steps": "Start", "content": "what is the weather in Goa?"}
{"steps": "Plan", "content": "I need to get weather for Goa"}
{"steps": "Tools", "content": "get_weather(goa)"}
{"steps": "output", "content": "The weather in Goa is sunny with a temperature of 25 degrees Celsius"}
"""

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return f"Could not get weather for {city}"

# Initialize message history
message_history = [
    {"role": "system", "content": System_prompt}
]

user_query = input(">")
message_history.append({"role": "user", "content": user_query})

while True:
    # Get AI response
    response = client.chat.completions.create(
        model="models/gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )
    
    ai_response = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": ai_response})
    paredResult = json.loads(ai_response)
    
    if(paredResult.get("steps") == "Start"):
        print("Starting llm...", paredResult.get("content"))
        continue
    if(paredResult.get("steps") == "Plan"):
        print("Planning...", paredResult.get("content"))
        continue
    if(paredResult.get("steps") == "Tools"):
        print("Using tools...", paredResult.get("content"))
        tool_call = paredResult["content"]
        
        city = tool_call.split("(")[1].replace(")", "").replace('"', '')
        
        weather_result = get_weather(city)
        
        message_history.append({
            "role": "assistant",
            "content": weather_result
        })
        continue
    if(paredResult.get("steps") == "output"):
        print("Output...", paredResult.get("content"))
        break
    
   
    