from django.contrib import admin

from modelos.models import UploadedDocument

@admin.register(UploadedDocument)
class UploadedDocumentAdmin(admin.ModelAdmin):
    list_display       = ('id','title')
    search_fields      = ['id','title']
    list_display_links = ('id','title')
