📘 company-policy-agent (Agentic RAG with Milvus + Ollama + LangGraph)

A fully functional Agentic RAG (Retrieval-Augmented Generation) system that answers questions about internal company policies using:

Zilliz Cloud (Milvus)

LangGraph (Agent Workflow)

Ollama (Local LLM)

Web Search + Web Scraping Tools

PDF Ingestion + Chunking + Embeddings

This project demonstrates a modern tool-using AI agent capable of:
✔ reasoning
✔ planning
✔ multi-step retrieval
✔ external web search
✔ document lookup
✔ and final answer generation

🚀 Features
🔹 1. Internal RAG (Company Policies)

PDF is processed and chunked

Embeddings stored in Zilliz Cloud

Fast vector search for policy-related queries

🔹 2. Agentic Reasoning (LangGraph)

The agent follows this workflow:

START → Plan → Internal Retrieval → External Retrieval → Answer → END

🔹 3. Tool-Using Agent

If internal data is missing → uses a web search tool

If URL is found → uses a web scraping tool

Combines internal + external info

🔹 4. Local LLM (Ollama)
Uses:
ollama run llama3

🔹 5. Streamlit Frontend

Clean UI where users can ask questions.

🏗️ Architecture


                           ┌────────────────┐
                           │  User Query    │
                           └───────┬────────┘
                                   │
                                   ▼
                      ┌────────────────────────┐
                      │       PLAN NODE        │
                      │  (Break into subqs)    │
                      └─────────┬──────────────┘
                                │
                    ┌───────────▼──────────┐
                    │  INTERNAL RETRIEVAL  │
                    │  (Milvus Vector DB)  │
                    └───────────┬──────────┘
                                │
                ┌───────────────▼─────────────────┐
                │   EXTERNAL RETRIEVAL (Tools)     │
                │   Web Search + Web Scraper       │
                └───────────────┬─────────────────┘
                                │
                      ┌─────────▼─────────┐
                      │  ANSWER NODE      │
                      │  (Ollama LLM)     │
                      └───────┬──────────┘
                              │
                             END

                             📁 Project Structure
company-policy-agent/
│
├── data/
│   └── company_policies.pdf
│
├── milvus_zilliz.py
├── process_pdf.py
├── retrieval.py
├── web_search.py
├── web_scraper.py
├── agent.py
├── app.py
├── README.md
└── requirements.txt

⚙️ Setup Instructions
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Start Ollama

Download model:

ollama pull llama3


Run the model:

ollama run llama3

3️⃣ Configure Zilliz Cloud

Edit:

milvus_zilliz.py


Enter:

ZILLIZ_ENDPOINT

ZILLIZ_API_KEY

4️⃣ Ingest PDF Into Milvus
python process_pdf.py

5️⃣ Run the Streamlit app
streamlit run app.py

🧪 Example Questions to Ask

Try these:

"How many paid leaves are allowed per year?"

"Summarize WFH policy."

"What happens if I come late 5 times?"

"What is the notice period?"

"What is the password rotation rule?"

"Explain leave policy and WFH policy together."

"If internal info is missing, search the web for more details."

🧠 How Agentic RAG Works
✔ Planning

Breaks the question into 2–3 sub-questions.

✔ Internal Document Retrieval

Uses Milvus vector-search for policy PDFs.

✔ External Tool Use

If internal data is insufficient → performs:

Web search

Web scraping

✔ Final Answer

Ollama LLM merges:

internal policy info

external info

reasoning

🛠️ Technologies Used
Component	Technology
Agent Workflow	LangGraph
LLM	Ollama (llama3)
Vector DB	Zilliz Cloud / Milvus
Embeddings	SentenceTransformers
Frontend	Streamlit
Tools	Web Search + Web Scraper
⭐ Future Improvements

Multi-PDF knowledge base

Citations with source mapping

Hybrid search (keyword + vector)

Reflection agent (self-correction)

Chat memory

Admin dashboard for HR

🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first to discuss the ideas.

📜 License

MIT License.
