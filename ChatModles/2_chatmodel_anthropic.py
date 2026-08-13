from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

chat = ChatAnthropic(model="claude-3.5-sonnet-20241022")

result=chat.invoke("what is capital of India")
print(result)
print(result.content)