from app.services.vector_store import VectorStore

from app.core.config import settings


class Retriever:

    def __init__(self):

        self.vector_store = VectorStore()

    def retrieve(self, query : str, top_k: int | None = None):

        top_k = top_k or settings.TOP_K

        results = self.vector_store.search(
            query=query,
            top_k=top_k
        )

        documents = results.get(
            "documents",
            [[]]
        )[0]

        metadatas = results.get(
            "metadatas",
            [[]]
        )[0]

        outputs = []

        for document , metadata in zip(document,metadatas):
            outputs.append(
                {
                    "text":document,
                    "metadata":metadata
                }
            )
            
        return outputs