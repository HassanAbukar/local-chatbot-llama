from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

Answer the quetion bellow

here is a conversation history{history}

Question = {question}

Answer:

"""
modal = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | modal

# my_message = "Hellow. how are you?"
# result = chain.invoke({"question" : my_message})
# print(result)

def handle_conversation():
    history = ""
    print("Aske anything. Type (exit to quite)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        result = chain.invoke({"history" : history,"question" : user_input})
        print("Bot:", result)
        history += f"\nUser:{user_input}\nBot: {result}"


if __name__ == "__main__":
    handle_conversation()