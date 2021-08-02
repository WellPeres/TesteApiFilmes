from django.db import models
from uuid import uuid4

# Create your models here.

def upload_image_filme(instance, filename):
    return f"{instance.id_filme}-{filename}"

class Filmes(models.Model):
    id_filme = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    direct_by = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_filme, blank=True, null=True)
    
