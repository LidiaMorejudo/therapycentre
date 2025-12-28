from django.db import models


class Inquiry(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Inquiry from {self.name}"
