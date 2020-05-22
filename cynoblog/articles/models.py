from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from simple_history.models import HistoricalRecords
from django.core.validators import RegexValidator

import re
# Create your models here.

class Article(models.Model):

    title_validator = RegexValidator(r'(?=(^(.*?[\w \d \s].*?){50,}$))(?=(^.{1,200}$))',
                                        message="Article cannot be longer than 200 characters and cannot have more than 150 symbols.")
    title = models.CharField(max_length=200, validators=[title_validator,],)
    slug = models.SlugField(default='', editable=False)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    history = HistoricalRecords()
    # add in thumbnail later

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title')
        ]

    def __str__(self):
        return self.title

    def snippet_title(self):
        return self.title[:30] + "..."

    def snippet_desc(self):
        return self.desc[:50] + "..."
    
    def save(self,  *args, **kwargs):
        value = self.title
        self.slug = self.generate_unique_slug(Article, value)
        super().save(*args, **kwargs)
    
    def is_max_comments(self):
        comment_count = self.comments.all().count()
        return (comment_count >= 50)

    
    def generate_unique_slug(self, klass, field):
        """
        return unique slug if origin slug is exist.
        eg: `foo-bar` => `foo-bar-1`

        :param `klass` is Class model.
        :param `field` is specific field for title.
        """
        origin_slug = slugify(field, allow_unicode=True)
        unique_slug = origin_slug
        numb = 1
        while klass.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
        return unique_slug
