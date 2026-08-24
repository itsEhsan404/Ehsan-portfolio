from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    technologies = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="projects/", blank=True)

    @property
    def technology(self):
        return self.technologies

    @technology.setter
    def technology(self, value):
        self.technologies = value

    def __str__(self):
        return self.title
