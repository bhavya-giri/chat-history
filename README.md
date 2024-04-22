# chat-history
Storing chat history of your RAG Pipelines like ChatGPT, also accessing previous context in conversation.

This project is based on the blog post ["Storing Chat History like ChatGPT for your RAG Pipeline with previous context - LlamaIndex, FastAPI"](https://medium.com/@bhavyagiri/storing-chat-history-like-chatgpt-for-your-rag-pipeline-with-previous-context-llamaindex-fastapi-ca775a325473) written by me.


## Demo Video
https://github.com/bhavya-giri/chat-history/assets/102273412/4ae5bd72-a223-4b49-8720-2a7e48828c33



## Run Locally

### Backend

Go to the backend directory

```bash
  cd backend
```
Create and activate virtual environment

```bash
  python -m venv .venv
  source .venv/bin/activate
```
Install dependencies

```bash
  pip install -r requirements.txt
```
Rename .env.example to .env and update the environment variables with your configuration.

```bash
  mv .env.example .env
```
Start the server

```bash
  uvicorn src.main:app --reload
```

### Frontend

Go to the frontend directory

```bash
  cd frontend
```

Install dependencies

```bash
  npm install
```

Start the app

```bash
  npm run dev
```

Then head to http://localhost:5173/chat




