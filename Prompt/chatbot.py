from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model= "gemini-3.5-flash")

chat_histroy=[
   SystemMessage(content="you are a helpful ai assitant")
]
while True:
   user_input= input("you:")
   chat_histroy.append(HumanMessage(content=user_input))
   if user_input == "exit":
      break
   result= model.invoke(chat_histroy)
   chat_histroy.append(AIMessage(content=result.content))
   print("AI:",result.content)

print(chat_histroy)   
      
