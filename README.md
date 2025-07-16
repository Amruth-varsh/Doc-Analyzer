# Agentic RAG Chatbot (LLaMA 3.2)

A modular, agent-based chatbot for answering questions about your own documents. It uses Retrieval-Augmented Generation (RAG) and Meta’s LLaMA 3.2 (via Ollama) to provide accurate, context-aware answers. The system supports multiple document formats and uses semantic search for fast, relevant retrieval.

---

## What is this project?

This project is an **Agentic RAG Chatbot** that allows you to upload documents (PDF, CSV, PPTX, DOCX, TXT, MD) and ask questions about their content in natural language. It combines:
- **Document Ingestion:** Load and process your files.
- **Semantic Search:** Find relevant information using FAISS and embeddings.
- **LLM Reasoning:** Use LLaMA 3.2 (via Ollama) to generate answers based on retrieved context.
- **Agentic Pipeline:** Modular agents handle retrieval, LLM response, memory, and more.
- **User Interface:** Simple Gradio web UI for easy interaction.

---

## How does it work?

1. **Ingestion:** You upload documents. The system splits them into chunks and creates vector embeddings for each chunk.
2. **Indexing:** Embeddings are stored in a FAISS vector database for fast similarity search.
3. **Question Answering:**
   - When you ask a question, the system finds the most relevant document chunks.
   - These are sent, along with your question, to LLaMA 3.2 running locally via Ollama.
   - The LLM generates a context-aware answer, citing sources when possible.
4. **Memory:** The chatbot can remember previous interactions for a more natural conversation.

---

## Quick Start

Follow these steps to set up and run the chatbot:

1. **Clone the repository**
   - Download the code to your computer:
     ```bash
     git clone https://github.com/Amruth-varsh/Doc-Analyzer.git
     cd Doc-Analyzer
     ```
2. **Create and activate a virtual environment**
   - This keeps dependencies isolated:
     ```bash
     python -m venv venv
     # On Windows
     venv\Scripts\activate
     # On Linux/Mac
     source venv/bin/activate
     ```
3. **Install Python dependencies**
   - Install all required packages:
     ```bash
     pip install -r requirements.txt
     ```
4. **Download and run Ollama**
   - Ollama is required to run LLaMA 3.2 locally.
   - Download Ollama: https://ollama.com/download
   - Start the LLaMA 3.2 model:
     ```bash
     ollama run llama3.2
     ```
   - Make sure this stays running in a separate terminal window.
5. **Run the chatbot**
   - Start the web interface:
     ```bash
     python app.py
     ```
   - Open the provided local URL in your browser to use the chatbot.

---

## Example Use Cases
- Ask questions about research papers, manuals, or meeting notes.
- Summarize large documents quickly.
- Extract key facts or data from multiple file types.

---

## Troubleshooting
- **Ollama not found?** Make sure you downloaded and started Ollama before running the chatbot.
- **Model not loading?** Ensure you have enough system resources and the correct model name (`llama3.2`).
- **Dependency errors?** Double-check you are in the virtual environment and all packages installed successfully.

---


