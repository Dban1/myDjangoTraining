from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from .import forms
from comments.forms import CommentForm
from .models import Comment

# Create your views here.

def comment_edit(request, id):
    comment = Comment.objects.get(pk=id)
    original_body = str(comment.body)
    article = comment.article
    comment_form = CommentForm()

    if request.user != comment.author:
        return redirect('articles:list')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form = comment_form.save()
            return HttpResponseRedirect(reverse('articles:detail', args=[article.slug]))
    return render(request, 'comments/comment_edit.html', {'comment': comment, 'original_body': original_body, 'form': comment_form})

def comment_delete(request, id):
    comment = Comment.objects.get(pk=id)
    original_body = str(comment.body)
    article = comment.article

    if request.user != comment.author:
        return redirect('articles:list')

    if request.method == 'POST' and request.user == comment.author:
        print(request.POST)
        if request.POST.get('delete') == 'Confirm':
            instance = Comment.objects.filter(id=id)
            instance.delete()
        
        return HttpResponseRedirect(reverse('articles:detail', args=[article.slug]))
        
        
    return render(request, 'comments/comment_delete.html', {'comment': comment, 'original_body': original_body,})