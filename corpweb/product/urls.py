from django.urls import path
from .views import PartsView, ProductGoalView, ProductView, download_sample

app_name='product'

urlpatterns=[
    path('<str:product_name>/',ProductView.as_view(), name='product_detail'),
    path('1/product_goal/',ProductGoalView.as_view(), name='product_goal'),
    path('1/parts/',PartsView.as_view(), name='parts'),
    path('1/download_sample',download_sample, name='download_sample')
    
]