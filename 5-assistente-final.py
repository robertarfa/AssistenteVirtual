#langchain padroniza o acesso as LLM
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, YoutubeLoader

# 1. Carregue as variáveis do arquivo .env
load_dotenv()
# 2. Acesse a API Key do ambiente
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_do_bot(lista_mensagens, documento):
  mensagem_system = '''
  Você é um assistente inteligente, você utiliza as seguintes informações para suas respostas: {informacoes}
  '''
  mensagens_modelo = [('system', mensagem_system)]
  
  mensagens_modelo += lista_mensagens

  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  return chain.invoke({'informacoes': documento}).content

def carrega_site():
  url_site = input('Digite a url do site: ')
  loader = WebBaseLoader(url_site)
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento = documento + doc.page_content
  return documento

def carrega_pdf():
  caminho = '/content/drive/MyDrive/curso_ia_python/arquivos/RoteiroViagemEgito.pdf'
  loader = PyPDFLoader(caminho)
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento = documento + doc.page_content
  return documento

def carrega_youtube():
  url_youtube = input('Digite a url do vídeo: ')
  loader = YoutubeLoader.from_youtube_url(url_youtube, language=['pt'])
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento = documento + doc.page_content
  return documento


print('Bem-vindo ao ChatBot da Robs! Digite "sair" para sair')

texto_selecao = '''Digite 1 se você quiser conversar com um site\n 
Digite 2 se você quiser conversar com um PDF\n 
Digite 3 se você quiser conversar com um vídeo do youtubw
'''

while True:
  selecao = input(texto_selecao)
  if selecao == '1':
    documento = carrega_site()
    break
  if selecao == '2':
    documento = carrega_pdf()
    break
  if selecao == '3':
    documento = carrega_youtube()
    break
  print("Digite um valor entre 1 e 3")

mensagens = []
while True:
  pergunta = input('Usuário: ')
  if pergunta.lower() == 'sair':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_do_bot(mensagens, documento)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('\nMuito obrigado por utilizar o RobsBot!')