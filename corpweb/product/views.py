from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.

class ProductView(generic.DetailView):
    model=Product
    context_object_name='product'
    template_name='product/product.html'
    
    def get_object(self, queryset=None):
        return Product.objects.get(name=self.kwargs['product_name'])
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    