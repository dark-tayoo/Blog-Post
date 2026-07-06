from django.shortcuts import render
from rest_framework import generics

from .serializers import BlogPostSerializer
from .models import BlogPost

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset = BlogPost.objects.all()
     serializer_class = BlogPostSerializer
     lookup_field = "pk"
    

# Create your views here.
