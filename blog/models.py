from django.db import models

# Create your models here.

class post(models.Model):
    
    CATEGORY_CHOICES=[
        ('python' , 'python'),
        ('backend' , 'backend'),
        ('django' , 'django'),
        ('git' , 'git'),
    ]
    
    title=models.CharField( max_length=200)
    content=models.TextField()
    category=models.CharField( max_length=100)
    image=models.ImageField(upload_to="blog/" , blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    
