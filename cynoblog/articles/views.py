import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import ArticleSerializer

from .models import Article
from .import forms
from comments.forms import CommentForm
from comments.serializers import CommentSerializer

import xlrd

IMPORT_FILE_TYPES = ['.xlsx', '.csv']

# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset= Article.objects.all().order_by('-date')
    serializer_class = ArticleSerializer

    @action(detail=True)
    def comments(self, request, *args, **kwargs):
        comment_list = Article.objects.get(pk=kwargs.get('pk')).comments.all()
        comment_serializer = CommentSerializer(comment_list, many=True)
        # json = JSONRenderer().render(comment_serializer.data)
        return Response(comment_serializer.data)


# def article_list(request):
#     articles = Article.objects.all().order_by('-date') #order by date
#     return render(request, 'articles/article_list.html', {'articles': articles})

# def article_details(request, slug):
#     article = get_object_or_404(Article, slug=slug)
#     comments = article.comments.all()
#     new_comment = None
#     comment_form = CommentForm()
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if article.is_max_comments():
#             raise Exception("This article has reached its comment limit.")
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = article
#             new_comment.author = request.user
#             comment_form = new_comment.save()

#     return render(request, 'articles/article_detail.html', {'article': article,
#                                                             'comments': comments,
#                                                             'new_comment':new_comment,
#                                                             'comment_form': comment_form})

# @login_required(login_url="/accounts/login/")
# def article_create(request):
#     if request.method == 'POST':
#         form = forms.CreateArticle(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             return redirect('articles:list')
#     else:
#         form = forms.CreateArticle()
#     return render(request, 'articles/article_create.html', {'form': form})

# @login_required(login_url="/accounts/login/")
# def article_delete(request, id):
#     article = Article.objects.get(pk=id)
#     original_body = article.desc
#     author = article.author

#     if request.method == 'POST' and request.user == author:
#         if request.POST.get('delete') == 'Confirm':
#             instance = Article.objects.filter(id=id)
#             instance.delete()
        
#         return redirect('articles:list')
        
        
#     return render(request, 'articles/article_delete.html', {'article': article, 'original_body': original_body,})

# def article_upload(request):
#     template = "articles/article_upload.html"
#     form = forms.UploadFileForm()

#     if request.method == 'GET':
#         return render(request, template, {'form': form})
    
#     csv_file = request.FILES['file']

#     if not csv_file.name.endswith('csv') or not csv_file.name.endswith('xlsx'):
#         messages.error(request, "Only .csv anf .xlsx files are supported.")

#     if csv_file.name.endswith('csv'):
#         data_set = csv_file.read().decode('UTF-8')
#         io_string = io.StringIO(data_set)
#         next(io_string) # skips header
#         for col in csv.reader(io_string, delimiter=',', quotechar="|"):
#             _, created = Article.objects.update_or_create(
#                 title = col[0],
#                 desc = col[1],
#                 author = request.user
#             )
#     elif csv_file.name.endswith('xlsx'):
#         form = forms.UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             workbook = xlrd.open_workbook(file_contents=file.read(), on_demand=True)
#             worksheet = workbook.sheet_by_index(0)

#             first_row = ['title', 'desc']
#             data = []
#             for row in range(1, worksheet.nrows):
#                 elm = {}
#                 for col in range(worksheet.ncols):
#                     elm[first_row[col]] = worksheet.cell_value(row, col)
#                 data.append(elm)
            
#             for article in data:
#                 form = forms.CreateArticle(article)
#                 if form.is_valid():
#                     instance = form.save(commit=False)
#                     instance.author = request.user
#                     instance.save()
#         return redirect('articles:list')

#     return redirect('articles:list')

