from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
import streamlit as st

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura a API Key do Groq
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# Inicializa o modelo de linguagem
chat = ChatGroq(model='llama-3.1-70b-versatile')

# Define o título da aplicação
st.title('Analisador de Vídeos do YouTube')

# Cria os campos de entrada
url_youtube = st.text_input('Insira o link do vídeo:', placeholder='https://www.youtube.com/watch?v=...')
pergunta = st.text_input('Insira sua pergunta sobre o vídeo:', placeholder='Faça um resumo do vídeo')


# Processa a requisição quando o usuário insere a URL e a pergunta
if url_youtube and pergunta:
    try:
        # Carrega o conteúdo do vídeo com o YoutubeLoader
        loader = YoutubeLoader.from_youtube_url(url_youtube, language=['pt'])
        lista_documentos = loader.load()

        # Concatena o conteúdo de todos os documentos em uma única string
        document = '\n'.join([doc.page_content for doc in lista_documentos])

        # Define o template da mensagem para o modelo de linguagem
        template = ChatPromptTemplate.from_messages([
            ('system', 'Você é um assistente amigável e tem acesso às seguintes informações para formular suas respostas: {documentos_informados}'),
            ('user', '{input}')
        ])

        # Cria a cadeia de prompts e obtém a resposta do modelo
        chain = template | chat
        resposta = chain.invoke({'documentos_informados': document, 'input': pergunta})

        # Exibe a resposta na interface
        # st.text_input('Título do vídeo:', resposta)
        st.text_area("Resposta:", resposta.content, height=800, disabled=True)

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar a solicitação: {e}")