from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title')
        ]