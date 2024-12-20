from django.urls import path

from notebook.views.index import index, upload_document




urlpatterns = [
    path("", index, name="index"),
    path("upload_document", upload_document, name="upload_document"),
]