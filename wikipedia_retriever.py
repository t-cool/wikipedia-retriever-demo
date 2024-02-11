from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever()

docs = retriever.get_relevant_documents(query="HUNTER X HUNTER")

print(docs[0].page_content[:400])

# https://python.langchain.com/docs/integrations/retrievers/wikipedia#examples