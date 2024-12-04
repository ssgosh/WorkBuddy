from prompt_toolkit import PromptSession
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings

# Create a PromptSession object
session = PromptSession()

# Define a key binding to accept input with Ctrl-Enter (Ctrl-M)
bindings = KeyBindings()

@bindings.add('c-d')  # c-m is the key combination for Ctrl-Enter
def _(event):
    "Accept input on Ctrl-Enter."
    event.current_buffer.validate_and_handle()

def multiline_input():
    print("Enter your text (Ctrl-Enter to finish):")
    text = session.prompt(multiline=True, key_bindings=bindings)
    return text

# Get the multiline input
text = multiline_input()
print("\nYour entered text:")
print(text)
