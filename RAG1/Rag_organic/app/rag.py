# from retriever import retriever
# from model import model


# def ask(question: str):

#     docs = retriever.invoke(question)

#     context = "\n\n".join(
#         doc.page_content for doc in docs
#     )

#     pages = sorted(
#         {doc.metadata["page"] for doc in docs}
#     )

#     prompt = f"""
# You are an Organic Chemistry tutor.

# Answer ONLY from the provided context.

# If the answer is not found, say:

# "I couldn't find this information in the textbook."

# Context:

# {context}

# Question:

# {question}

# Answer:
# """

#     response = model.invoke(prompt)

#     return response.content, pages

from retriever import retriever
from model import model


def ask(question: str):
    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    pages = sorted(
        {doc.metadata["page"] + 1 for doc in docs}   # +1 because PDF pages start from 0
    )

    prompt = f"""
You are an expert Organic Chemistry teacher.

Use ONLY the context below to answer.

If the answer is not present, say:
"I couldn't find this information in the textbook."

Context:
{context}

Question:
{question}
"""

    response = model.invoke(prompt)

    return response.content, pages
