from django.urls import path

from notebook.views.index import index




urlpatterns = [
    path("", index, name="index")
]