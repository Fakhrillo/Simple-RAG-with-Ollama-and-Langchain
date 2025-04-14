# 🧠 LangChain Pizza Review Q&A Bot

This is a LangChain-based Question and Answer chatbot that can answer questions about a pizza restaurant using real customer reviews.

> 🧑‍🏫 **Based on Tech With Tim’s tutorial**:  
> Original Source: [LangChain + Ollama Tutorial](https://www.youtube.com/watch?v=E4l91XKQSgw)  
>  
> 🔧 **Modifications**:  
> - Replaced **Pandas** with **Polars** for better performance and lower memory usage.
> - Used [`uv`](https://github.com/astral-sh/uv) for fast dependency resolution and isolated environment.

---

## 📂 Project Structure
├── main.py              # Main chatbot logic
├── vector.py            # Vector store creation and retriever setup
├── realistic_restaurant_reviews.csv  # Input data (CSV of reviews)
├── chroma_langchain_db/ # Persisted Chroma DB (created after first run)
├── README.md            # This file

---

## 🚀 Features

- Built with **LangChain**, **Ollama**, and **Chroma** for efficient RAG (Retrieval-Augmented Generation).
- Uses **LLaMA 3.2** locally via Ollama to generate answers.
- Retrieves the most relevant customer reviews before generating answers.
- Conversational loop that lets users ask multiple questions.
- Embeds and persists documents for efficient vector similarity search.
- Fast setup using `uv`, a modern Python package manager.

---

## ⚙️ Setup Instructions

### 1. Install [Ollama](https://ollama.com)

Pull the model if you haven’t already:

```bash
ollama pull llama3.2
```

---

### 2. Use uv for Environment Setup (Recommended)

If you have uv installed:

```bash
uv sync
```

If you don’t have **uv**:

❗Don’t have **uv**?
    Install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  #macOS and Linux

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  #Windows
```

Or use the regular way:
```bash
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

### 3. Run the Bot
```bash
uv run main.py
```

or 

```bash
python3 main.py

or 

py main.py # In Windows
```

---

### 🧠 How It Works
1. CSV Parsing: Loads realistic_restaurant_reviews.csv with Polars for fast, efficient data reading.
2. Embedding: Combines the review title and body, then embeds it using llama3.2.
3. Vector Store: Saves the embeddings into a persistent Chroma vector store.
4. Retriever: For any question, it pulls the top 5 most relevant reviews.
5. LLM: Uses those reviews + question to generate a precise, contextual answer.

---

### Example

```
Ask your question (q to quit): What do people say about the staff?

----------------------------------------------------------------
Answer:
Most customers mention the staff is friendly and attentive. Some reviews highlight the welcoming atmosphere created by the team.
```

---

### 📚 Credits
• 🧠 LLM via [Ollama](https://ollama.com)
• 🔍 Vector DB via [Chroma](https://www.trychroma.com)
• 🧪 Tutorial by Tech With Tim: [YouTube Video](https://www.youtube.com/watch?v=E4l91XKQSgw)
• 🧹 Performance Optimization: [Polars](https://pola.rs)
• ⚡ Dependency & Env Management: [`uv`](https://github.com/astral-sh/uv)

---

### 📜 License

This project is open-sourced for educational and demonstration purposes. Please credit original authors and tutorial sources if sharing or modifying.

---

### 💡 Ideas to Extend
• Build a web front-end using Streamlit or Gradio.
• Add filters (e.g., rating thresholds, review date ranges).
• Store user question history or allow session-based memory.

