from django.shortcuts import render
from django.views import generic

from product.models import Product

from .models import Notice

# Create your views here.
class NoticeListView(generic.ListView):
    model=Notice
    template_name='notice/bulletin_board.html'
    context_object_name='notice_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset, **kwargs)
    
    
class NoticeDetailView(generic.DetailView):
    model=Notice
    template_name='notice/notice_detail.html'
    context_object_name='notice'