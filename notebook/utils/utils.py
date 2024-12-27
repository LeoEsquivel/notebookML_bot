import re
import pdfplumber
from docx import Document
from transformers import pipeline

# qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
qa_pipeline = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")



def extract_text(file_path: str) -> str:
    if file_path.endswith('.pdf'):

        with pdfplumber.open(file_path) as pdf:
            return ''.join(page.extract_text() for page in pdf.pages)
        
    elif file_path.endswith('docx'):
        doc = Document(file_path)
        return '\n'.join(paragraph.text for paragraph in doc.paragraphs)
    else:
        raise ValueError("Formato de archivo no compatible. Solo se adminten .PDF y .DOCX")
    

def generate_answer(context: str, question: str) -> str:
    try:
        result = qa_pipeline(question=question, context=context)
        print(result)
        return result["answer"]
    except Exception as e:
        return f'Error al generar la respuesta: {str(e)}'
    

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text