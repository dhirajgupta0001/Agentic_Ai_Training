from rag import ask

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer, pages = ask(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSource Pages:", pages)
