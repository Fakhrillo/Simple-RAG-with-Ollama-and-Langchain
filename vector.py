from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import polars as pl

df = pl.read_csv('realistic_restaurant_reviews.csv')

embeddings = OllamaEmbeddings(model="llama3.2")

db_location = './chroma_langchain_db'
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []

    ids = []

    for i, row in enumerate(df.iter_rows(named=True)):
        document = Document(
            page_content= row["Title"] + " " +row["Review"],
            metadata= {'rating': row["Rating"], 'date': row['Date']},
            id= str(i)
        )

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)


retriever = vector_store.as_retriever(
    search_kwargs={'k':5}
)