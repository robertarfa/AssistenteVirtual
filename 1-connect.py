#langchain padroniza o acesso as LLM
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

# 1. Carregue as variáveis do arquivo .env
load_dotenv()
# 2. Acesse a API Key do ambiente
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.1-70b-versatile')

resposta = chat.invoke("Olá, modelo. Qual seu nome?")

print(resposta.content)

from langchain.prompts import ChatPromptTemplate