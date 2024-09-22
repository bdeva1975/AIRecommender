import json
from recommendations_lib import get_collection

def populate_collection(collection_name, source_json_file):
    collection = get_collection("./data/chroma", collection_name)
    
    if collection.count() == 0:
        with open(source_json_file) as json_file:
            source_json = json.load(json_file)
            
            ids = [str(i) for i in range(len(source_json))]
            documents = [f"{item['name']}\n\n{item['description']}" for item in source_json]
            metadatas = [{"name": item['name'], "url": item['url']} for item in source_json]
            
            collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
    
    print(f"Populated collection {collection_name}")
    
    return collection

if __name__ == "__main__":
    populate_collection('services_info', 'data/services_info.json')