#langchain padroniza o acesso as LLM
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os
from langchain_community.document_loaders import PyPDFLoader

# 1. Carregue as variáveis do arquivo .env
load_dotenv()
# 2. Acesse a API Key do ambiente
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.1-70b-versatile')

path = path = r"D:\OneDrive\CURSOS\PROJETOS\Dados\AssistenteVirtual\curso_introducao_python_para_ia\arquivos\RoteiroViagemEgito.pdf"

loader = PyPDFLoader(path)

#sempre retorna lista
lista_documentos = loader.load()

print(lista_documentos[0].page_content)

document = ''
for doc in lista_documentos:
  document += doc.page_content
  print(document)

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável e tem acesso as seguinte informações para formular suas respostas: {documentos_informados}'),
    ('user', '{input}')
])

chain = template | chat
resposta = chain.invoke({'documentos_informados': document, 'input': 'Quantos dias são ideiais?'})

print(resposta.content)