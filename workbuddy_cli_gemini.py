import os
import google.generativeai as genai
from dotenv import load_dotenv
# import readline

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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
  system_instruction="Your task is to classify a webpage as \"work\" or \"non-work\", based on the page title, page body text, and page URL. This will be used to moderate content on a user's web browser using an extension, to help them stay focused on work-related activities only. Some of those fields may be empty. Input format is json, like: { \"page_title\" : \"\", \"page_body\" : \"\", page_url : \"\" } . You should only output a json containing the classification, and an explanation to the end-user for why the page belongs to that category. Out format: { \"category\" : \"\", \"explanation\" : \"\"} . ",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "{\"page_title\" :  \"Untitled prompt | Google AI Studio\"}",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"category\": \"work\",\n  \"explanation\": \"The page title contains 'Google AI Studio', which suggests a platform for AI development or related work tasks.\"\n}\n```\n",
      ],
    },
  ]
)

exit = False
while not exit:
    print('Enter JSON {"page_title" : "", "page_url" : "", "page_content" : ""}')
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
        except KeyboardInterrupt:
            exit = True
            break
    if not exit:
        msg = '\n'.join(lines)
        response = chat_session.send_message(msg)
        print(response.text)
    
