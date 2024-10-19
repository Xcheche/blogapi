from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    

    class Meta:
       
     
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
