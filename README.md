

# <img src="https://github.com/user-attachments/assets/d12ab57e-0456-42ee-bf44-f4c3d2810284" style="width:30px; height:auto;"> WorkBuddy


<!-- ![983049](https://github.com/user-attachments/assets/d12ab57e-0456-42ee-bf44-f4c3d2810284) -->

***An LLM-based content moderator***

Firefox extension to block webpages unrelated to work, based on page title and URL. Local LLMs with Ollama and Langchain to ensure your browsing history never leaves your device, for complete privacy. Google Gemini also supported.


<!-- ![copilot_image_1733637667810](https://github.com/user-attachments/assets/3f0b32b5-1658-4473-b558-d93b0ae715c7) -->
<img src="https://github.com/user-attachments/assets/3f0b32b5-1658-4473-b558-d93b0ae715c7" style="width:50%; height:auto; display:block; margin-left:auto; margin-right:auto;">



<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [<img src="https://github.com/user-attachments/assets/d12ab57e-0456-42ee-bf44-f4c3d2810284" style="width:30px; height:auto;"> WorkBuddy](#img-srchttpsgithubcomuser-attachmentsassetsd12ab57e-0456-42ee-bf44-f4c3d2810284-stylewidth30px-heightauto-workbuddy)
  - [Features](#features)
    - [Updates](#updates)
  - [Installation & Usage](#installation--usage)
  - [Customization](#customization)
  - [Screenshot](#screenshot)
    - [Block Page](#block-page)
    - [Developer Console messages for non-blocked page](#developer-console-messages-for-non-blocked-page)
  - [Internals](#internals)
  - [CLI invocation for testing](#cli-invocation-for-testing)
  - [Attribution](#attribution)

<!-- /code_chunk_output -->



## Features

- Blocks webpages automatically on page load
- Displays a block page with the page URL and title, along with an explanation for blocking
- For non-blocked pages, the explanation for not blocking is available in the developer console

### Updates

- Now works with **local LLMs**. Your browsing history stays **completely private!**
  - Tested with LLama 3.2:1b and 3.2:3b
  - Implemented using Ollama and Langchain
  - No GPU required! Tested on a consumer-grade Intel CPU laptop.

## Installation & Usage

1. Install python packages
```bash
pip install -r requirements.txt
```
2. Put your Google Gemini API key in `.env` or as environment variable `GEMINI_API_KEY`
3. Start the WorkBuddy server
```bash
python workbuddy_server.py
```
4. Go to `about:debugging` in Firefox -> `Load Temporary Addons` -> Select the `manifest.json` file under extension/firefox
5. Open any non-work relaed webpage (e.g. reddit.com). WorkBuddy should block it

## Customization

Change the text in `prompts/system_instruction.txt` to customize which webpages get blocked. Current contents are:

> Your task is to classify a webpage as "work" or "non-work", based on the page title, page body text, and page URL. This will be used to moderate content on a user's web browser using an extension, to help them stay focused on work-related activities only. Some of those fields may be empty. Input format is json, like: { "page_title" : "", "page_body" : "", page_url : "" } . You should only output a json containing the classification, and an explanation to the end-user for why the page belongs to that category. Output format: { "category" : "", "explanation" : ""} .
>
> The person is mainly involved in Computer Science and Artificial Intelligence related Research and Engineering, which may also include software development. Front pages of search engines or video search websites, such as Google and YouTube, are categorized as work. Relevant lecture videos are considered work, but pop-science videos are not. Forums such as Reddit or Twitter are considered non-work. However, discussion threads on very particular subjects may be considered work, such as a thread on matrix factorization techniques, or on enabling particular VSCode features. Gmail and other email sites are considered work. News sites, including Tech news, are considered non-work. Relevant academic publications are considered work.

## Screenshot

### Block Page
![image](https://github.com/user-attachments/assets/82739cca-c238-49dc-b36b-14de79772d6b)

### Developer Console messages for non-blocked page

![image](https://github.com/user-attachments/assets/6458d2f1-eb4c-442d-a76b-97ff822ea092)


## Internals

- Server runs on Flask
- uses Google Gemini API 
- No auth needed as of now
- REST API
  - POST /classify, with json content, containing { "page_title" : "", "page_body" : "", page_url : "" }
  - In response, return {"category" : "", "explanation" : ""}
- Workflow:
  - WorkBuddy Firefox addon extracts title and URL upon page load, and sends it to the WorkBuddy server
  - WorkBUddy server contacts Google Gemini via API and asks it to return page category and an explanation for the categorization, and relays it back to the addon
  - The addon replaces current page with block page if category is "non-work", and displays the explanation on the block page

## CLI invocation for testing

Interactive cli-based chat can be used for testing out the system prompt. Uses `prompt-toolkit`.
```bash
python workbuddy_cli_gemini.py
```

## Attribution

<a href="https://www.flaticon.com/free-icons/angel" title="angel icons">Angel icons created by Freepik - Flaticon</a>
