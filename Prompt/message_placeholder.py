from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


#chatTemplate

chat_Template= ChatPromptTemplate(
    [
        ('system', 'you are a helpful customer Support agent'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{query}'),
    ]
)


chat_history=[]
#load chathistroy
with open ('chat_history.txt')as f:
 chat_history.extend(f.readlines())   
 print(chat_history)

#create prompt

 prompt=chat_Template.invoke({'chat_history':chat_history,'query':"what is my refund"})

print(prompt)