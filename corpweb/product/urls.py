from django.urls import path
from .views import ProductView

app_name='product'

urlpatterns=[
    path('<str:product_name>/',ProductView.as_view(), name='product_detail')
]