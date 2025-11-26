from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from milvus_zilliz import setup_collection, client, COLLECTION_NAME

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_text(text, chunk=400, overlap=80):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def store_pdf_in_milvus(pdf_path="data/company_policies.pdf"):
    setup_collection()

    print("📄 Reading PDF...")
    text = load_pdf(pdf_path)

    print("✂️ Splitting text...")
    chunks = split_text(text)

    print("🔢 Embedding...")
    vectors = model.encode(chunks).tolist()

    print("🧠 Storing in Zilliz Cloud...")

    # *** FIX: Convert to row-wise format ***
    rows = []
    for vec, txt in zip(vectors, chunks):
        rows.append({
            "vector": vec,
            "text": txt
        })

    client.insert(
        collection_name=COLLECTION_NAME,
        data=rows
    )

    print("✅ Done! PDF stored successfully.")

if __name__ == "__main__":
    store_pdf_in_milvus()
