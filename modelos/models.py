from django.db import models

class UploadedDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed_text = models.TextField(blank=True, null=True) 

