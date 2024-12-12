from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    #     "temperature": 1,
    # "top_p": 0.95,
    # "top_k": 40,
    # "max_output_tokens": 8192,
    top_p=0.95,
    top_k=40,
    format="json",
)


def load_prompt(fname):
    with open(fname, "r") as f:
        return "".join(f.readlines())


system_instruction = load_prompt("./prompts/system_instruction.txt")
for msg in [
    ("human", '{"page_title" : "ChatOllama - LangChain Documentation",'
     ' "page_url" : "https://python.langchain.com/v0.2/api_reference/'
     'ollama/chat_models/langchain_ollama.chat_models.ChatOllama.html"}'),
    ("human", '{"page_title" : "IND vs AUS | Live from Brisbane: '
     'Rohit\'s position still undecided? | AUS practice updates", '
     '"page_url" : "https://www.youtube.com/watch?v=bebfsoL9viY"}'),
     ("human", '{"page_title" : "model temperature llm - Google Search"}')]:

    messages = [
        ("system", system_instruction), msg
    ]
    output = llm.invoke(messages)
    print(output)

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

# messages = [
#     ("system", "You are a helpful translator. Translate the user sentence to French."),
#     ("human", "I love programming."),
# ]
# output = llm.invoke(messages)

# print(output)
