from django.urls import path
from .views import InquiryCreateView, InquirySuccessView

app_name='inquiry'

urlpatterns = [
    path('',InquiryCreateView.as_view(),name='inquiry'),
    path('success/',InquirySuccessView.as_view(),name='success')
]