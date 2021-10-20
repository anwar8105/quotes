from django.db import models

# Create your models here.


class AutherQ(models.Model):
    author = models.TextField(max_length=25)
    quote = models.TextField()

    def __str__(self):
        return self.quote[:70]
