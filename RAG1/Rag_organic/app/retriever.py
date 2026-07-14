# from langchain_chroma import Chroma
# from embeddings import embeddings

# db = Chroma(
#     persist_directory="./db",
#     embedding_function=embeddings,
# )

# retriever = db.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k":5,
#         "fetch_k":20,
#     }
# )

# query = "Explain Sandmeyer's reaction in haloalkanes."

# docs = retriever.invoke(query)

# for i, doc in enumerate(docs, start=1):
#     print(f"\n===== Result {i} =====")
#     print(f"Page: {doc.metadata.get('page')}")
#     print(doc.page_content[:500])

# from langchain_chroma import Chroma
# from embeddings import embeddings

# db = Chroma(
#     persist_directory="./db",
#     embedding_function=embeddings,
# )

# results = db.similarity_search_with_score(
#     query="Sandmeyer reaction",
#     k=10,
# )

# for i, (doc, score) in enumerate(results, start=1):
#     print("=" * 70)
#     print(f"Rank : {i}")
#     print(f"Score: {score}")
#     print(f"Page : {doc.metadata['page']}")
#     print(doc.page_content[:400])

# collection = db.get()

# for doc, meta in zip(collection["documents"], collection["metadatas"]):
#     if "Sandmeyer" in doc or "Sandmeyer’s" in doc:
#         print("=" * 70)
#         print(meta)
#         print(doc[:500])

from langchain_chroma import Chroma
from embeddings import embeddings

db = Chroma(
    persist_directory="./db",
    embedding_function=embeddings,
)

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":5,
        "fetch_k":20,
    },
)
