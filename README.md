from langchain_community.retrievers import WikipediaRetriever
from IPython.display import display, JSON

retriever = WikipediaRetriever()

docs = retriever.get_relevant_documents(query="HUNTER X HUNTER")

display(JSON(docs))
