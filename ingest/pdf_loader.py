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

# pip install pytesseract pdf2image pillow

import pytesseract
from pdf2image import convert_from_path

def extract_text_from_scanned_pdf(pdf_path, lang='fra'):
    """
    Extrait le texte d'un PDF scanné via OCR.

    Args:
        pdf_path (str): Chemin vers le fichier PDF scanné.
        lang (str): Langue pour l'OCR (ex: 'fra' pour français, 'eng' pour anglais).

    Returns:
        str: Texte complet extrait du PDF.
    """
    try:
        # Convertir chaque page du PDF en image
        pages = convert_from_path(pdf_path)
        full_text = ""

        # Appliquer l'OCR sur chaque page
        for page_number, page in enumerate(pages, 1):
            text = pytesseract.image_to_string(page, lang=lang)
            full_text += f"--- Page {page_number} ---\n{text}\n"

        return full_text

    except Exception as e:
        print(f"Erreur lors de l'extraction OCR: {e}")
        return ""
