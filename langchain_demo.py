from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0,
    #     "temperature": 1,
    # "top_p": 0.95,
    # "top_k": 40,
    # "max_output_tokens": 8192,
    top_p=0.95,
    top_k=40,
    # format="json",
)

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "Translate the following sentence from {input_language} to {output_language}:",
#         ),
#         ("human", "{input}"),
#     ]
# )

# chain = prompt | llm
# output = chain.invoke(
#     {
#         "input_language": "English",
#         "output_language": "Spanish",
#         "input": "I love programming.",
#     }
# )

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
output = llm.invoke(messages)

print(output)