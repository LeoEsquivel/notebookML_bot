from django.urls import path

from notebook.views.analyze_text import analyze_text
from notebook.views.chat import ask_question, chat
from notebook.views.index import index, upload_document




urlpatterns = [
    path("", index, name="index"),
    path("upload_document", upload_document, name="upload_document"),
    path('chat', chat, name='chat'),
    path("ask_question", ask_question, name="ask_question"),
    path("analyze_text", analyze_text, name="analyze_text"),
]