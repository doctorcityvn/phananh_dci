from django.urls import path

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('s2/', views.s2, name='s2'),
    path('s1/', views.s1, name='s1'),
    path('login1/', views.my_view, name='my_view'),
]
