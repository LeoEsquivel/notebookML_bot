import pdfplumber
from docx import Document

def extract_text(file_path: str):
    if file_path.endswith('.pdf'):

        with pdfplumber.open(file_path) as pdf:
            return ''.join(page.extract_text() for page in pdf.pages)
        
    elif file_path.endswith('docx'):
        doc = Document(file_path)
        return '\n'.join(paragraph.text for paragraph in doc.paragraphs)
    else:
        raise ValueError("Formato de archivo no compatible. Solo se adminten .PDF y .DOCX")