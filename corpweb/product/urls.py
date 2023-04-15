from django.urls import path
from .views import ProductGoalView, ProductView

app_name='product'

urlpatterns=[
    path('<str:product_name>/',ProductView.as_view(), name='product_detail'),
    path('1/product_goal/',ProductGoalView.as_view(), name='product_goal')
    
]