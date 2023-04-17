from django.http import FileResponse
from django.shortcuts import render
from django.views import generic
from .models import FacilityList, Parts, Press, Product, ProductGoal

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
    
class ProductGoalView(generic.DetailView):
    model=ProductGoal
    context_object_name='product_goal'
    template_name='product/goal.html'
    
    def get_object(self, queryset=None):
        return ProductGoal.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    

class PartsView(generic.DetailView):
    model=Parts
    context_object_name='parts'
    template_name='product/parts.html'
    
    def get_object(self, queryset=None):
        return Parts.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    
def download_sample(request):
    file_obj = Parts.objects.latest('created_at')
    file_path = file_obj.sample.path
    file_name= 'parts_sample.zip'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response

class FacilityListView(generic.DetailView):
    model=FacilityList
    context_object_name='facility_list'
    template_name='product/facility_list.html'
    
    def get_object(self, queryset=None):
        return FacilityList.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    
class PressView(generic.DetailView):
    model=Press
    context_object_name='press_list'
    template_name='product/press.html'
    
    def get_object(self, queryset=None):
        return Press.objects.all()
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)