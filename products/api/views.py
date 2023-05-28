from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from products.models import Products

class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()