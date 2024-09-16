from django.db import models

# Create your models here.

class Blogs(models.Model):
    title  = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', null=True)
    category = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
    