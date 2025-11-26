from sentence_transformers import SentenceTransformer
from milvus_zilliz import client, COLLECTION_NAME

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def search_policy(query, top_k=5):
    q_vec = embedder.encode([query])[0]

    results = client.search(
        collection_name=COLLECTION_NAME,
        data=[q_vec],
        limit=top_k,
        output_fields=["text"]
    )

    contexts = []
    
    # results is a LIST of hits, NOT nested inside ['hits']
    for hit in results[0]:
        # each hit has this structure:
        # { "id": ..., "distance": ..., "entity": { "text": "..." } }
        contexts.append(hit["entity"]["text"])

    return contexts
