from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from notice.models import Notice
from product.models import Product

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
        
        context = super(HomeView, self).get_context_data(product_queryset=product_queryset, notice_news=notice_news, **kwargs)
        return context
    