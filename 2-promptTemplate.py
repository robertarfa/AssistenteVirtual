from langchain.prompts import ChatPromptTemplate


template = ChatPromptTemplate.from_messages(
  [('user', 'Traduza {expressao} para o idioma {idioma}')]
)

print(template)

resposta = template.invoke({'expressao': 'Beleza?', 'idioma': 'inglês'})



