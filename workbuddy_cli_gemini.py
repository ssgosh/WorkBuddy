import os
import google.generativeai as genai
from dotenv import load_dotenv

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
    print('Enter JSON {"page_title" : "", "page_url" : "", "page_content" : ""} (Ctrl-D to finish):')
    text = session.prompt(multiline=True, key_bindings=bindings)
    return text


# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}


def load_prompt(fname):
    with open(fname, "r") as f:
        return "".join(f.readlines())


system_instruction = load_prompt("./prompts/system_instruction.txt")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction,
)


chat_session = model.start_chat()
while True:
    # Get the multiline input
    msg = multiline_input()
    response = chat_session.send_message(msg)
    print(response.text)
