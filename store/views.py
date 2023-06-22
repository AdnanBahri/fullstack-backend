from rest_framework import generics, permissions as permissions_rest
from .models import Category, Product as ProductModel
from .serializers import CategorySerializer, ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions_rest.AllowAny]


class Product(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions_rest.AllowAny]
    lookup_field = "slug"


class CategoryItemView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions_rest.AllowAny]

    def get_queryset(self):
        return ProductModel.objects.filter(
            category__in=Category.objects.get(
                slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=0)
    serializer_class = CategorySerializer
    permission_classes = [permissions_rest.AllowAny]
