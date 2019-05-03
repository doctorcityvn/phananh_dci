from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from center import views
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', views.menu, name='menu'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signup1/', views.signup1, name='signup1'),
    path('signup2/', views.signup2, name='signup2'),
    path('menu/', views.menu, name='menu'),
    path('menu_user/', views.menu_user, name='menu_user'),
    path('menu_doctor/', views.menu_doctor, name='menu_doctor'),
    path('menu_center/', views.menu_center, name='menu_center'),
    path('menu_data/', views.menu_data, name='menu_data'),
    path('login1/', views.login1, name='login1'),
    path('test/', views.Test, name='Test'),
    path('test5/<slug:slug>/', views.Test5, name='Test5'),

    path('aj/<slug:slug>/', views.aj, name='aj'),
    path('aj1/validate_username/', views.validate_username, name='validate_username'),
    path('alluser/', views.alluser, name='alluser'),
    path('datlenh/', views.datlenh, name='datlenh'),
    path('testnhanlenh/', views.testnhanlenh, name='testnhanlenh'),
    path('user/', views.user1, name='user1'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('staff/', views.Staff, name='Staff'),
    path('a2/<slug:slug>/', views.thu1, name='thu1'),
    path('all/<slug:slug>/', views.cacphong1, name='cacphong1'),
    path('khoa/', views.Khoa, name='Khoa'),
    path('khoa/<slug:slug>/', views.Khoa1, name='Khoa1'),
    path('printer/<slug:slug>/', views.print1, name='print1'),
    path('khoa/all/<slug:slug>/', views.Khoa, name='Khoa'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
