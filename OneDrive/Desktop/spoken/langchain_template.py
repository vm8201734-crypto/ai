from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama    
model_name="llama3.2:latest "
llm = ChatOllama(model=model_name)
while True:
    role = input("User: ")
    topic = input("Topic: ")
    if role.lower() == "exit" or topic.lower() == "exit":
        break


    reactive=ChatPromptTemplate.from_messages([
        {("System", "You are a {role} that helps answer questions about {topic}.")}
    ]
    )
    prompt=reactive.invoke(role=role, topic=topic)
    cons=llm.invoke(prompt)
    print(f"Assistant: {cons.content}")

if __name__ == "__main__":
    pass
