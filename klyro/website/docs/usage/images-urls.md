---
parent: Usage
nav_order: 700
description: Add images and web pages to the klyro coding chat.
---

# Images & web pages

You can add images and URLs to the klyro chat.

## Images

Klyro supports working with image files for many vision-capable models
like GPT-4o and Claude 3.7 Sonnet.
Adding images to a chat can be helpful in many situations:

- Add screenshots of web pages or UIs that you want klyro to build or modify.
- Show klyro a mockup of a UI you want to build.
- Screenshot an error message that is otherwise hard to copy & paste as text.
- Etc.

You can add images to the chat just like you would
add any other file:

- Use `/add <image-filename>` from within the chat
- Use `/paste` to paste an image from your clipboard into the chat.
- Launch klyro with image filenames on the command line: `klyro <image-filename>` along with any other command line arguments you need.

## Web pages

Klyro can scrape the text from URLs and add it to the chat.
This can be helpful to:

- Include documentation pages for less popular APIs.
- Include the latest docs for libraries or packages that are newer than the model's training cutoff date.
- Etc.

To add URLs to the chat:

- Use `/web <url>`
- Just paste the URL into the chat and klyro will ask if you want to add it.

You can also scrape web pages from the command line to see the markdown version that klyro produces:


```
python -m klyro.scrape https://klyro.chat/docs/usage/tips.html
```
