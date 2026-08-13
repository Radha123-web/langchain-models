from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents=["What is the capital of France?",
      "What is the capital of India?",
      "What is the capital of USA?"]

result= embedding.embed_documents(documents)
print(str(result))