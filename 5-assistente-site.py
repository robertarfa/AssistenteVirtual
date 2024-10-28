#langchain padroniza o acesso as LLM
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os
from langchain_community.document_loaders import WebBaseLoader

# 1. Carregue as variáveis do arquivo .env
load_dotenv()
# 2. Acesse a API Key do ambiente
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.1-70b-versatile')

loader = WebBaseLoader("https://www.collabtranslation.com/")

#sempre retorna lista
lista_documentos = loader.load()

# print(lista_documentos[0].page_content)

document = ''
for doc in lista_documentos:
  document += doc.page_content
  print(doc)

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado Collab e tem acesso as seguinte informações para dar as suas respostas: {documentos_informados}'),
    ('user', '{input}')
])

chain = template | chat
resposta = chain.invoke({'documentos_informados': document, 'input': 'Quais trabalhos são oferecidos?'})

print(resposta.content)