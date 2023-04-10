from django.urls import path
from .views import NoticeDetailView, NoticeListView


app_name='notice'

urlpatterns=[
    path('',NoticeListView.as_view(),name='bulletin_board'),
    path('detail/<int:pk>',NoticeDetailView.as_view(), name='detail')
]