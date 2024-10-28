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

def resposta_do_bot(lista_mensagens):
  mensagens_modelo = [('system', 'Você é um assistente de receitas culinárias saudáveis e fáceis, além dos itens, mostre o modo de preparo')]
  # user_message = [('user', 'Traduza {expressao} para o idioma {idioma}')]

  mensagens_modelo += lista_mensagens

  template = ChatPromptTemplate.from_messages(
     mensagens_modelo
  )
  chain = template | chat
  return chain.invoke({}).content

print('Bem-vindo ao ChatBot de culinária da Robs! (Digite x se você quiser sair!)\n')
mensagens = []
while True:
  pergunta = input('Usuário: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_do_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('\nMuito obrigado por utilizar o RobsBot!')