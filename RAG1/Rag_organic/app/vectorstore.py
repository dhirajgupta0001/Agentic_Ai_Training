from langchain_chroma import Chroma
import shutil
import os

DB_PATH = "./db"

def create_vectorstore(chunks, embeddings):

    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH,
    )

    return db
