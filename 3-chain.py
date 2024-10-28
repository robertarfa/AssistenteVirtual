#langchain padroniza o acesso as LLM
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os

# 1. Carregue as variáveis do arquivo .env
load_dotenv()
# 2. Acesse a API Key do ambiente
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.1-70b-versatile')

template = ChatPromptTemplate.from_messages(
  [
    ('system', 'Você é um assistente que sempre responde com frases de exemplo para utilizar a palavra'),
    ('user', 'Traduza {expressao} para o idioma {idioma}')
   ]
)

chain = template | chat

resposta = chain.invoke({'expressao': 'Belelza?', 'idioma': 'inglês'})

print(resposta.content)