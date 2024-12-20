from django.http import JsonResponse
from django.shortcuts import render

from modelos.models import UploadedDocument


def index(request):
    context={}
    return render(request, 'index.html', context)


def upload_document(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            document = UploadedDocument.objects.create(
                title=file.name,
                file=file
            ).save()
            return JsonResponse({'msg': 'Archivo subido correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({"msg": "Error al subir el archivo", "error": e}, status=400)
