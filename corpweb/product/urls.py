from django.urls import path
from .views import FacilityListView, PartsView, PressView, ProductGoalView, ProductView, download_sample

app_name='product'

urlpatterns=[
    path('<str:product_name>/',ProductView.as_view(), name='product_detail'),
    path('1/product_goal/',ProductGoalView.as_view(), name='product_goal'),
    path('1/parts/',PartsView.as_view(), name='parts'),
    path('1/download_sample',download_sample, name='download_sample'),
    path('1/facility_list/',FacilityListView.as_view(), name='facility_list'),
    path('1/press/',PressView.as_view(), name='press')
    
]