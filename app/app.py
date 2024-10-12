from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import pandas as pd

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Loading documents
documents = SimpleDirectoryReader(
    "data"
    ).load_data()

# Create index
index = VectorStoreIndex.from_documents(documents, show_progress=True)

query_engine = index.as_query_engine()

response = query_engine.query("Find an email from TLDR AI")

print(response)



