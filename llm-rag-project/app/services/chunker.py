from app.core.config import settings

class TextChunker:
    def __init__(self,chunk_size:int | None = None,overlap:int| None = None):
        self.chunk_size =(
            chunk_size
            or settings.CHUNK_SIZE
        )
        self.overlap = (
            overlap
            or settings.CHUNK_OVERLAP
        )

    def split(self,text : str)->list[str]:

        chunks = []

        start = 0        

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunk = chunk.strip()

            if chunk:
                chunks.append(chunk)

            start = end - self.overlap
        return chunks