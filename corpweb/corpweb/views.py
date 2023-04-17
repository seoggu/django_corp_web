from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import render
from django.views import generic
from company.models import MainSlide
from notice.models import Notice
from product.models import Product
from company.models import MainInfo

def home_view(request):
    product_queryset = Product.objects.all()
    context = {
        'product_queryset':product_queryset
    }
    return render(request, 'home.html', context)

class HomeView(generic.TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        product_queryset = Product.objects.all()
        notice_news = Notice.objects.filter(Q(division='option0') | Q(division='option1'))
        maininfo = MainInfo.objects.all()
        mainslide = MainSlide.objects.latest('created_at')
        
        
        context = super(HomeView, self).get_context_data(product_queryset=product_queryset, notice_news=notice_news, maininfo=maininfo,mainslide=mainslide, **kwargs)
        return context
    
def download_brochure(request):
    file_obj = MainInfo.objects.latest('created_at')
    file_path = file_obj.brochure.path
    file_name= 'YUCHANG.pdf'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response
    