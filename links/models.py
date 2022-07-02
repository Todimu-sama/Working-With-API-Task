from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Link(models.Model):
    targetUrl = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    createdDate = models.DateTimeField(editable=False)
    active = models.BooleanField(default=True)

