from  langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()



llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

parser= JsonOutputParser()
template= PromptTemplate(

    template="give me the name,age,city of a fictional person\n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}

)

# prompt= template.format()
# result= model.invoke(prompt)
# print(result)
# final_result= parser.parse(result)
# print(final_result)
# print(type(final_result))
# python json object ko dic ki tarh treat krta h

# hum isko chins m bhi create krt skte hain

chain =template|model|parser
result= chain.invoke({})
print(result)