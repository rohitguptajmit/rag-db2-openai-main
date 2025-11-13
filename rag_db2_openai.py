import os
from dotenv import load_dotenv, dotenv_values
from openai import OpenAI
import pandas as pd
import spacy
import trafilatura

from itables import init_notebook_mode  # safe even if run in script
init_notebook_mode(all_interactive=True)  # no-op in non-notebook environments

# ---- 1. Load environment variables ----
load_dotenv(".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMBED_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in .env")

client = OpenAI()

# ---- 2. OpenAI helper functions ----
def get_embedding(text: str):
    text = text.replace("\n", " ")
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return resp.data[0].embedding  # list[float]


def chat_with_context(context: str, question: str) -> str:
    system_prompt = (
        "You are a knowledgeable assistant. Answer the question "
        "based solely on the provided context. "
        "If the information is not in the context, say "
        "'The information is not available in the provided context.'"
    )
    user_msg = f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"

    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.2,
        max_tokens=512,
    )
    return resp.choices[0].message.content

# ---- 3. Connect to Db2 using db2.ipynb helpers (if in notebook, skip here) ----
# In a pure script you can use ibm_db directly, but since you already have db2.ipynb,
# we keep the notebook as the main entry point for interactive work.
# This script focuses on the core RAG logic and is mirrored in the notebook.
