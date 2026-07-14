# app/debug_db.py

from langchain_chroma import Chroma
from embeddings import embeddings

db = Chroma(
    persist_directory="./db",
    embedding_function=embeddings,
)

print(db._collection.count())
