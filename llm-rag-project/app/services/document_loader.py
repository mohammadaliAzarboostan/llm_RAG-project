from pathlib import Path

from pypdf import PdfReader

class DocumentLoader:

    def load_pdf(self,file_path : str):

        reader = PdfReader(file_path)

        documents = []

        for page_number, page in enumerate(reader.pages,start=1):

            text = page.extract_text() or ""

            text = text.strip()

            if not text:
                continue

            documents.append(
                {
                    "text":text,
                    "page":page_number
                }
            )
        return documents

loader = DocumentLoader()
