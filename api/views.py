from .serializers import (BlogPostSerializer, CategorySerializer, CommentSerializer)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from blog.models import (BlogPost, Category, Comment)


class BlogPostListAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]

class BlogPostRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class = [IsAdminUser]
    lookup_field = 'pk'



class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [IsAdminUser]
    lookup_field = 'pk'



class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

class CommentRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = []
    lookup_field = 'pk'

