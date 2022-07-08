from django.contrib.auth import get_user_model
from django.db import models
from . import utils


# Create your models here.
class Link(models.Model):
    targetUrl = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.identifier}"

    def save(self, *args, **kwargs):
        if not self.identifier:
            random_id = utils.generate_random_id()

            while Link.objects.filter(identifier=random_id).exists():
                random_id = utils.generate_random_id()

            self.identifier = random_id()

        super().save(*args, **kwargs)
