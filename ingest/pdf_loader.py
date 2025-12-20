import os
from pypdf import PdfReader

def load_pdfs_from_folder(folder_path: str) -> list:
    texts = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            reader = PdfReader(path)

            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

            texts.append(text)

    return texts
