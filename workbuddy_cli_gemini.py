import os
import google.generativeai as genai
from dotenv import load_dotenv  # type: ignore

# import readline

from prompt_toolkit import PromptSession
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a PromptSession object
session = PromptSession()

# Define a key binding to accept input with Ctrl-Enter (Ctrl-M)
bindings = KeyBindings()

@bindings.add("c-d")
def _(event):
    "Accept input on Ctrl-D."
    event.current_buffer.validate_and_handle()


def multiline_input():
    # print("Enter your text (Ctrl-D to finish):")
    print('Enter JSON {"page_title" : "", "page_url" : "", "page_content" : ""} (Ctrl-D to finish):')
    text = session.prompt(multiline=True, key_bindings=bindings)
    return text


# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    #   "response_mime_type": "text/plain",
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction='Your task is to classify a webpage as "work" or "non-work", based on the page title, page body text, and page URL. This will be used to moderate content on a user\'s web browser using an extension, to help them stay focused on work-related activities only. Some of those fields may be empty. Input format is json, like: { "page_title" : "", "page_body" : "", page_url : "" } . You should only output a json containing the classification, and an explanation to the end-user for why the page belongs to that category. Out format: { "category" : "", "explanation" : ""} . ',
)

# chat_session = model.start_chat(
#     history=[
#         {
#             "role": "user",
#             "parts": [
#                 '{"page_title" :  "Untitled prompt | Google AI Studio"}',
#             ],
#         },
#         {
#             "role": "model",
#             "parts": [
#                 '```json\n{\n  "category": "work",\n  "explanation": "The page title contains \'Google AI Studio\', which suggests a platform for AI development or related work tasks."\n}\n```\n',
#             ],
#         },
#     ]
# )

# exit = False
# while not exit:
#     print('Enter JSON {"page_title" : "", "page_url" : "", "page_content" : ""}')
#     lines = []
#     while True:
#         try:
#             line = input()
#             lines.append(line)
#         except EOFError:
#             break
#         except KeyboardInterrupt:
#             exit = True
#             break
#     if not exit:
#         msg = "\n".join(lines)
#         response = chat_session.send_message(msg)
#         print(response.text)

while True:
    # Get the multiline input
    text = multiline_input()
    response = chat_session.send_message(msg)
    print(response.text)
