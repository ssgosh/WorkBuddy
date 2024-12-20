import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory

def load_prompt(fname):
    with open(fname, "r") as f:
        return "".join(f.readlines())

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

system_instruction = load_prompt("./prompts/system_instruction.txt")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction,
)

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory('.', 'hello_gemini.html')

@app.route('/classify', methods=['POST'])
def classify_page():
    data = json.dumps(request.json, indent=4)
    print(data, type(data))
    response = model.generate_content(data)
    
    print(response.text, type(response.text))
    return jsonify(response.text)

if __name__ == '__main__':
    app.run(debug=True)





# import os
# import google.generativeai as genai
# from dotenv import load_dotenv


# def load_prompt(fname):
#     with open(fname, "r") as f:
#         return "".join(f.readlines())


# load_dotenv()
# genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 8192,
#     "response_mime_type": "application/json",
# }


# system_instruction = load_prompt("./prompts/system_instruction.txt")

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config,
#     system_instruction=system_instruction,
# )


# chat_session = model.start_chat()
# while True:
#     # Get the multiline input
#     msg = '''
#         {
#             "page_title" : "Download or install libraries to access Gemini",
#             "page_url" : "https://ai.google.dev/gemini-api/docs/downloads",
#         }
#     '''
#     response = chat_session.send_message(msg)
#     print(response.text)
