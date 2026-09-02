from django.db import models
from django.utils.text import slugify

# Create your models here.

class post(models.Model):

    CATEGORY_CHOICES=[
        ('python' , 'python'),
        ('backend' , 'backend'),
        ('django' , 'django'),
        ('git' , 'git'),
    ]
    
    title=models.CharField( max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content=models.TextField()
    category=models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='python'
        )
    image=models.ImageField(upload_to="blog/" , blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    
