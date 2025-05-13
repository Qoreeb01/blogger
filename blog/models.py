from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to= 'img/', null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank= True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'comments')
    created_on = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.title)

        self().save(*args, **kwargs)