from django.shortcuts import render
from django.views import generic

from product.models import Product
from .models import Introduction,History, MainBusiness, Map, OrganizationChart, Revenue

# Create your views here.
class IntroductionView(generic.DetailView):
    model=Introduction
    context_object_name='introduction'
    template_name='company/introduction.html'
    
    def get_object(self, queryset=None):
        # Return the specific object that you want to display
        return Introduction.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)

class HistoryView(generic.DetailView):
    model=History
    context_object_name='history'
    template_name='company/history.html'
    
    def get_object(self, queryset=None):
        return History.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    
class MainBusinessView(generic.DetailView):
    model=MainBusiness
    context_object_name='mainbusiness'
    template_name='company/mainbusiness.html'
    
    def get_object(self, queryset=None):
        return MainBusiness.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        mainbusiness = MainBusiness.objects.latest('created_at').business_list
        business_list= mainbusiness.split(',')
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, business_list=business_list,  **kwargs)
    
class OrganizationChartView(generic.DetailView):
    model=OrganizationChart
    context_object_name='organizationchart'
    template_name='company/organizationchart.html'
    
    def get_object(self, queryset=None):
        return OrganizationChart.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    
class MapView(generic.DetailView):
    model=Map
    context_object_name='map'
    template_name='company/map.html'
    
    def get_object(self, queryset=None):
        return Map.objects.latest('created_at')
    
    def get_context_data(self, **kwargs): 
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    
    
class RevenueView(generic.DetailView):
    model=Revenue
    context_object_name='revenue'
    template_name='company/revenue.html'
    
    def get_object(self, queryset=None):
        return Revenue.objects.latest('created_at')
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)