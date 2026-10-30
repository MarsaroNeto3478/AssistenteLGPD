"""Configurações do projeto, lidas do arquivo .env (ou de variáveis de ambiente).

Tudo que você vai querer mudar em experimentos fica aqui, num lugar só.
As outras partes do código leem `config.ALGUMA_COISA` na hora de usar,
então o script de avaliação consegue trocar um valor antes de rodar.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Pastas
DATA_DIR = os.getenv("DATA_DIR", "data")      # onde ficam os PDFs
DB_DIR = os.getenv("DB_DIR", ".chroma")       # onde o Chroma salva o índice
COLLECTION = "documentos"

# Embeddings: modelo multilíngue pequeno, roda bem em CPU
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-small")

# Divisão em trechos (em caracteres)
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))

# Quantos trechos mandar para o LLM
TOP_K = int(os.getenv("TOP_K", "4"))

# LLM: qualquer API no formato da OpenAI (Ollama, Gemini, Groq...)
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "ollama")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.1"))

# Textos da interface
APP_TITLE = os.getenv("APP_TITLE", "Assistente de documentos")
APP_DESCRIPTION = os.getenv(
    "APP_DESCRIPTION",
    "Pergunte sobre os documentos. Cada resposta mostra de qual arquivo e página veio.",
)
