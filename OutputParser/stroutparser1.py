from  langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
import os

print("Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm= HuggingFaceEndpoint(
   repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

#1st prompt--detailed Report
template1= PromptTemplate(
    template="write detailed Report on{topic}",
    input_variables={'topic'}
)

#2prompt---summary
template2= PromptTemplate(
    template="write a 5 line summary on the following text ./n{text}",
    input_variables={'text'}
)




parser=StrOutputParser()
chain=template1|model|parser|template2|model|parser

result=chain.invoke({'topic':"black hole"})

print(result)
