# WorkBuddy

***An LLM-based content moderator***

Blocks webpages unrelated to work based on page content

- [WorkBuddy](#workbuddy)
  - [MVP Features](#mvp-features)
    - [Extension](#extension)
    - [Server](#server)

---

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
- Should wait for
