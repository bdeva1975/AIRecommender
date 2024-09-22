import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from chromadb.utils import embedding_functions
import json

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_collection(path, collection_name):
    # Use OpenAI's text-embedding-ada-002 model for embeddings
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ.get("OPENAI_API_KEY"),
        model_name="text-embedding-ada-002"
    )
    
    client = chromadb.PersistentClient(path=path)
    collection = client.get_or_create_collection(collection_name, embedding_function=embedding_function)
    
    return collection

def get_vector_search_results(collection, question):
    results = collection.query(
        query_texts=[question],
        n_results=4
    )
    
    return results

def get_personalized_recommendation(question, description):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides personalized recommendations based on service descriptions."},
            {"role": "user", "content": f"Based on the following service description, please summarize how it addresses these requirements:\n\nService description: {description}\n\nRequirements: {question}"}
        ],
        model="gpt-3.5-turbo",
    )
    
    return chat_completion.choices[0].message.content

def get_similarity_search_results(question):
    # Initialize or get the collection
    collection = get_collection("./data/chroma", "services_info")
    
    search_results = get_vector_search_results(collection, question)
    
    num_results = len(search_results['documents'][0])
    
    results_list = []
    
    for i in range(num_results):
        personalized_recommendation = get_personalized_recommendation(question, search_results['documents'][0][i])
        
        results_list.append({
            'original': search_results['documents'][0][i],
            'summary': personalized_recommendation,
            'name': search_results['metadatas'][0][i]['name'],
            'url': search_results['metadatas'][0][i]['url'],
        })
    
    return results_list

# You can add a main block for testing if needed
if __name__ == "__main__":
    # Test the functions here
    pass