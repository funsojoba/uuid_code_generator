import uuid
from django.db import models


class CodeModel(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False)
    uuid_field = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
