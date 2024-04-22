# chat-history
Storing chat history of your RAG Pipelines like ChatGPT, also accessing previous context in conversation.

This project is based on the blog post 

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




