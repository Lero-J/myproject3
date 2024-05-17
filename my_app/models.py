from django.db import models
from django.db.models import F
# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=255)

    text = models.TextField(max_length=255)

    published_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['published_at']



    def __str__(self):
        return  f'{self.name} {self.published_at}'






