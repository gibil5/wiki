from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=16)
    title = models.CharField(max_length=16)
    content = models.CharField(max_length=128)

    def __str__(self):
        #return f"{self.name} {self.title}"
        return f"Page: {self.title}"
