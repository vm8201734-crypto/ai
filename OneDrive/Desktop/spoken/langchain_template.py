from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
model_name="llama3.2:latest"
llm = ChatOllama(model=model_name)
react_prompt = ChatPromptTemplate.from_messages([
    ("system", "{role}"), ("user", "{input}")
]
)
chain= react_prompt|llm| StrOutputParser()
while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    role = input("Enter role (e.g., 'You are a helpful assistant.'): ")
    if role.strip() == "":
        role = "You are a helpful assistant."
    output = chain.invoke({"role": role, "input": user_input})
    print(f"Assistant: {output}")
