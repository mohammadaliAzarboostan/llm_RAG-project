from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def embed_text(self,text : str):

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_documents(self, texts: list[str]):

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()