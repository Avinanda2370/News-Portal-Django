from django.urls import path
from news.views import first, singleview,catview

urlpatterns = [
    path('',first,name='first'),
    path('singleview/<int:pk>',singleview, name='singleview'),
    path('catview/<int:pk>',catview, name='catview')
    
   
]