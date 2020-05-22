from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from articles.models import Article
from simple_history.models import HistoricalRecords

import re

# Create your models here.

class Comment(models.Model):
    body_validator = RegexValidator(r'(?=.{32,})(?=.*[\d\w]+).*$', message="Needs at least 32 characters with at least one alphanumeric.")

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(validators=[body_validator,],)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="comments")
    history = HistoricalRecords(cascade_delete_history=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
