from django.contrib import admin

from modelos.models import Question, UploadedDocument

@admin.register(UploadedDocument)
class UploadedDocumentAdmin(admin.ModelAdmin):
    list_display       = ('id','title')
    search_fields      = ['id','title']
    list_display_links = ('id','title')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display       = ('id','question_text')
    search_fields      = ['id','question_text']
    list_display_links = ('id','question_text')
