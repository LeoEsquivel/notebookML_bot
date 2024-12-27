from django.db import models

class UploadedDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed_text = models.TextField(blank=True, null=True) 


class Question(models.Model):
    document      = models.ForeignKey(UploadedDocument, on_delete=models.CASCADE, related_name='question_uploadDocument')
    question_text = models.TextField()
    answer_text   = models.TextField(blank=True, null=True)
    create_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text