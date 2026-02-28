
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai.types import vector_store
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

embeddings = OpenAIEmbeddings(
         model="text-embedding-3-large",
    )
    
vector_store = QdrantVectorStore.from_existing_collection(
    collection_name="learning_rag",
    url="http://localhost:6333",
    embedding=embeddings
)
#ask something to the agent
user_query = input("User: ")

#search the vector store and get relevant chunks
search_result = vector_store.similarity_search(user_query)

context = "\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_result])


System_prompt = """ you are helpful assistant 
who can answer user query based on the context retrieved from the document
answer the question based on the context just provide the answer

Context: {context}
User Query: {user_query}

"""

openai_client = OpenAI()

response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": System_prompt.format(context=context, user_query=user_query)},
        {"role": "user", "content": user_query}
    ]
)

print(response.choices[0].message.content)
