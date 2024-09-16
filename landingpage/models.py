from django.db import models

# Create your models here.

from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    hero_photo = models.ImageField(upload_to='owner/', null=True, blank=True)
    photo = models.ImageField(upload_to='owner/', null=True, blank=True)
    slogan = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=500)
    skills = models.TextField(null=True, blank=True)
    service1 = models.CharField(max_length=50, null=True, blank=True)
    service2 = models.CharField(max_length=50, null=True, blank=True)
    service3 = models.CharField(max_length=50, null=True, blank=True)
    service4 = models.CharField(max_length=50, null=True, blank=True)
    service5 = models.CharField(max_length=50, null=True, blank=True)
    service6 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='testimonials')
    teller = models.CharField(max_length=100)
    testimonial = models.TextField(max_length=300)

    def __str__(self):
        return f"Testimonial by {self.teller}"
