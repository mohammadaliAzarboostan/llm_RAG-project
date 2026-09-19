from app.services.retriever import Retriever
from app.services.metis import MetisLLM

class RagService:
    def __init__(self):

        self.retriever = Retriever()
        self.llm = MetisLLM()

    def build_prompt(self,question:str,documents : list[dict]):

        context_parts = []

        for index , document in enumerate(documents,start=1):

            metadata = document["metadata"]

            source = metadata.get(
                "source",
                "unknown"
            )
            page = metadata.get(
                "page",
                "unknown"
            )

            context_parts.append(
                f"""
            SOURCE {index}
            FILE {source}
            PAGE {page}
            {document["text"]}
            """
            )
            context = "\n\n".join(
                context_parts
            )

            prompt = f"""
                You are a Retrieval Agumented Generation Assistant.

                Answer the user's question using ONLY
                the provided context.


                Context:

                {context}

                USER_QUESTION:
                {question}

                ANSWER:
            """

            return prompt

    def answer(self,question : str):

        documents = self.retriever.retrieve(question)

        if not documents:

            return{
                "answer":"No relevant information",
                "source":[]
            }
        prompt = self.build_prompt(question,documents)

        answer = self.llm.generate(prompt)

        sources = []

        for document in documents: 
            metadata = documents["metadata"]

            sources.append(
                {
                    "source":metadata.get(
                        "source"
                    ),
                    "page":metadata.get(
                        "page"
                    )
                }
            )

            return {
                "answer":answer,
                "sources":sources
            }