![983049](https://github.com/user-attachments/assets/d12ab57e-0456-42ee-bf44-f4c3d2810284)
# WorkBuddy

***An LLM-based content moderator***

Blocks webpages unrelated to work based on page content

- [WorkBuddy](#workbuddy)
  - [MVP Features](#mvp-features)
    - [Extension](#extension)
    - [Server](#server)
  - [Even more minimal features (CLI invocation)](#even-more-minimal-features-cli-invocation)

## MVP Features

We'll use a client-server architecture.
A local python server will receive page content/title.
It'll use LangChain to connect with ChatGPT or some other LLM.

### Extension

- Initial feature
  - Press a button to block the current page
- Press the button to send the current page's title to the server
  - Receive the category of the page ("work" or "non-work") and a one-sentence
  explanation from the server
  - Display a pop-up or a block page with the page category and the explanation

### Server

- Run on Flask
- No auth needed as of now
- REST API
  - POST /classify, with json content, containing { "page_title" : "", "page_body" : "", page_url : "" }
  - In response, return {"category" : "", "explanation"}

## Even more minimal features (CLI invocation)

- Receive input from stdin.
- Send request to OpenAI and classify as "work" or "non-work", and get explanation as json : { "category" : "", "explanation" : ""}
- Print the category and the explanation
- Continue receiving more input from the user

## Attribution

<a href="https://www.flaticon.com/free-icons/angel" title="angel icons">Angel icons created by Freepik - Flaticon</a>
