from django.db import models
from workspaces.models import Space
from django.utils.text import slugify

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
