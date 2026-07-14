from loader import load_pdf
from splitter import split_documents
from embeddings import embeddings
from vectorstore import create_vectorstore

documents = load_pdf("data/chemistry.pdf")
print(f"Loaded {len(documents)} pages")

chunks = split_documents(documents)
print(f"Created {len(chunks)} chunks")

db = create_vectorstore(chunks, embeddings)

print("Vector database created successfully!")
for chunk in chunks:
    if "Sandmeyer" in chunk.page_content:
        print("=" * 80)
        print(chunk.metadata)
        print(chunk.page_content)
