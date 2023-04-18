from django.http import FileResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from company.models import MainInfo

from product.models import Product
from .models import Inquiry
from .forms import InquiryCreationForm

# Create your views here.

class InquiryCreateView(generic.CreateView):
    model=Inquiry
    form_class=InquiryCreationForm
    context_object_name='inquiry'
    template_name='inquiry/inquiry.html'
    
    def get_success_url(self):
        return reverse_lazy('inquiry:success')
    
    def get_context_data(self, **kwargs):
        maininfo= MainInfo.objects.all()
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset,maininfo=maininfo, **kwargs)
    
class InquirySuccessView(generic.TemplateView):
    template_name='inquiry/inquiry_success.html'
    
    def get_context_data(self, **kwargs):
        maininfo= MainInfo.objects.all()
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset,maininfo=maininfo, **kwargs)


    
    