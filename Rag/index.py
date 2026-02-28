from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai.types import vector_store
from dotenv import load_dotenv
load_dotenv()

# Debug: Check if API key is loaded
import os
print(f"API Key loaded: {'YES' if os.getenv('OPENAI_API_KEY') else 'NO'}")

# Path to current directory (where PDF files are located)
path_pdf = Path(__file__).parent / "javascriptPdf.pdf"
loader = PyPDFLoader(path_pdf)
docs = loader.load()

# split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitted_docs = text_splitter.split_documents(docs)
# print(splitted_docs[12])

try:
    # create embeddings
    embeddings = OpenAIEmbeddings(
         model="text-embedding-3-large",
    )
    
    vector_store = QdrantVectorStore.from_documents(
        documents=splitted_docs,
        embedding=embeddings,
        url="http://localhost:6333",   # Qdrant running locally
        collection_name="learning_rag"
        )
    
    print("indexing of document done....")
    
except Exception as e:
    print(f"Error during indexing: {e}")
    print("Make sure you have OpenAI API key set as environment variable: OPENAI_API_KEY")