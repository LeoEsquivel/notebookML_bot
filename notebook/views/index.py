from django.http import JsonResponse
from django.shortcuts import render

from ayuda_botML.settings import MEDIA_ROOT
from modelos.models import UploadedDocument
from notebook.utils.utils import extract_text


def index(request):
    context={}
    return render(request, 'index.html', context)


def upload_document(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            document = UploadedDocument.objects.create(
                title=file.name,
            )

            file_path = f'{MEDIA_ROOT}/{document.title}'

            try:
                texto_extraido = extract_text(file_path)
                document.processed_text = texto_extraido
                document.save()
            except ValueError as e:
                return JsonResponse({"msg": "Error al subir el archivo", "error": e}, status=400)

            return JsonResponse({'msg': 'Archivo subido correctamente', 'text': texto_extraido, 'document_id': document.id}, status=200)
    
        except Exception as e:
            return JsonResponse({"msg": "Error al subir el archivo", "error": e}, status=400)
    
    return JsonResponse({"msg": "Método no permitido"}, status=405)
