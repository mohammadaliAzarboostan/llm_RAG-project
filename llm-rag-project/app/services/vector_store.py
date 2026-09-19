import chromadb

from app.core.config import settings
from app.services.embeddings import EmbeddingService

class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH
        )

        self.embedding_services = EmbeddingService()

    def add_documents(self,texts: list[str],metadatas:list[dict], ids : list[str]):

        embeddings = self.embedding_services.embed_documents(texts)

        self.collection.add(
            documents = texts,
            embeddings = embeddings,
            metadatas = metadatas,
            ids = ids
        )

    def search(self, query : str, top_k: int):

        query_embedding = (
            self.embedding_services.embed_text(query)
        )

        results = self.collection.query(
            query_embeddings = [query_embedding],
            n_results = top_k
        )

        return results