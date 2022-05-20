from email.policy import default

from django.db import models
from accounts.models import Doctor

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    upload_date=models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/', default='heart.jpg')
    blog=models.TextField(max_length=6500)

    def __str__(self):
        return self.title