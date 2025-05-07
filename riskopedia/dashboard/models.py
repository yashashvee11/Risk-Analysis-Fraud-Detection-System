from django.db import models

# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to='transactions/')
    dataType = models.CharField(max_length=15, default='unstructured')
    content = models.TextField()

    def __str__(self):
        return str(self.document)
