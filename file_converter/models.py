from django.db import models
from django.utils import timezone
import os
import uuid
from django.conf import settings
# Create your models here.



def upload_to(instance, filename):
    return os.path.join('uploads', str(instance.file_uuid), filename)

class FileUpload(models.Model):
    file_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    original_file_extension = models.CharField(max_length=10)
    original_file_path = models.CharField(max_length=255)
    converted_files = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.uploaded_at} - {self.file_uuid}'






