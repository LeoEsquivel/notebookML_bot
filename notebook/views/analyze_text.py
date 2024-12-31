import json
from django.http import JsonResponse

from modelos.models import UploadedDocument
from notebook.utils.utils_resume import generate_summary
from notebook.utils.utils_spcy import find_entities_key_terms

# Spacy Model

def analyze_text(request):
    print('analyze_text')
    if request.method == 'POST':

        data = json.loads(request.body)

        file_id = data.get('file_id')

        try:
            document = UploadedDocument.objects.get(id=file_id)
        except UploadedDocument.DoesNotExist:
            return JsonResponse({"msg": "Documento no encontrado"}, status=404)
        
        result = find_entities_key_terms(document.processed_text)
        summary = generate_summary(document.processed_text)

        # print("Entidades detectadas:")
        # for categoria, valores in result["entities"].items():
        #     print(f"{categoria}: {', '.join(valores)}")

        # print("\n\n\nTerminos clave:")
        # print(", ".join(result["key_terms"]))


        return JsonResponse({
            "msg": "Ok",
            "entities": result,
            "summary": summary
        }, status=200)
    
    return JsonResponse({"msg": "Método no permitido"}, status=405)
