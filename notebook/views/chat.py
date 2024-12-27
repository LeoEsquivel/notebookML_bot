import json
import traceback
from django.http import JsonResponse
from django.shortcuts import render

from modelos.models import Question, UploadedDocument
from notebook.utils.utils import generate_answer


def chat(request):
    context={}
    context['files_list'] = UploadedDocument.objects.all()
    return render(request, 'chat.html', context)


def ask_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            document_id = data.get('document_id') 
            question_text = data.get('question')
            try:
                document = UploadedDocument.objects.get(id=8)
            except UploadedDocument.DoesNotExist:
                return JsonResponse({"msg": "Documento no encontrado"}, status=404)
            
            answer = generate_answer(document.processed_text, question_text)

            # question = Question.objects.create(
            #     document=document,
            #     question_text=question_text,
            #     answer_text=answer
            # )

            return JsonResponse({
                "msg": "Pregunta procesada correctamente",
                "question": question_text,
                "answer": answer
            }, status=200)

        except Exception as e:
            print(traceback.format_exc())
            print(e)
            return JsonResponse({"msg": "Error al procesar la pregunta", "error": str(e)}, status=400)

    return JsonResponse({"msg": "Método no permitido"}, status=405)