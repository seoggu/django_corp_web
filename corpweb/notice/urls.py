from django.urls import path
from .views import NoticeDetailView, NoticeListView, download_file


app_name='notice'

urlpatterns=[
    path('',NoticeListView.as_view(),name='bulletin_board'),
    path('detail/<int:pk>',NoticeDetailView.as_view(), name='detail'),
    path('download_file/<int:pk>',download_file, name='download_file')
]