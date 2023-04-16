

from django.urls import path
from .views import IntroductionView,HistoryView, MainBusinessView, MapView, OrganizationChartView, RevenueView


app_name='company'

urlpatterns=[
    path('introduction/',IntroductionView.as_view(), name='introduction'),
    path('history/',HistoryView.as_view(), name='history'),
    path('mainbusiness/',MainBusinessView.as_view(), name='mainbusiness'),
    path('organizationchart/',OrganizationChartView.as_view(), name='organizationchart'),
    path('map/',MapView.as_view(),name='map'),
    path('revenue/',RevenueView.as_view(), name='revenue')
]