from  langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()



llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='fact 3 about the topic'),
]
parser = StructuredOutputParser.from_response_schemas(schema)
template= PromptTemplate(

    template="give  3 fact about{topic}\n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)
# prompt = template.invoke({"topic":"balck hole"})
# result= model.invoke(prompt)
# final_result= parser.parse(result.content)
# print(final_result)

chain=template|model|parser
result=chain.invoke({"topic":"ai"})
print(result)
