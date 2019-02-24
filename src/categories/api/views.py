# All resource operation of CRUD
from rest_framework import viewsets

from .serializers import CategorySerializer
from categories.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# for each operation of CRUD

# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView
# )

# class CategoryListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CategoryDetailView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryCreateView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryUpdateView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDeleteView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

