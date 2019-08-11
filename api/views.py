from django.shortcuts import render

# Create your views here.
from blogging.models import Post, Category
from rest_framework import viewsets
from api.serializers import PostSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
