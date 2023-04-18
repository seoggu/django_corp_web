import os
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from company.models import MainInfo

from product.models import Product

from .models import Notice

# Create your views here.
class NoticeListView(generic.ListView):
    model=Notice
    template_name='notice/bulletin_board.html'
    context_object_name='notice_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        maininfo= MainInfo.objects.all()
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset,maininfo=maininfo, **kwargs)
    
    
class NoticeDetailView(generic.DetailView):
    model=Notice
    template_name='notice/notice_detail.html'
    context_object_name='notice'
    
    def get_context_data(self, **kwargs):
        maininfo= MainInfo.objects.all()
        product_queryset = Product.objects.all()
        return super().get_context_data(product_queryset=product_queryset,maininfo=maininfo, **kwargs)
    
def download_file(request, pk):
    obj = get_object_or_404(Notice, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, str(obj.file)) # get the path to the file
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type='application/octet-stream') # adjust content type as needed
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response