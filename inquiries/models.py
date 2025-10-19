from django.db import models

class Inquiries(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Inquiries from {self.name}"

