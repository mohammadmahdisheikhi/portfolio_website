from django.db import models

# Create your models here.

class Works (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, null=True)
    image1 = models.ImageField(upload_to='works/', null=True)
    image2 = models.ImageField(upload_to='works/', null=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title