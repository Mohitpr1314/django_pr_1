from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name ='homepage'),
    path('contact/', views.contactpage, name = 'contact'),
    path('package/', views.packagepage, name = 'package'),
    path('gallery/', views.gallerypage, name = 'gallery'),
    path('saveenquiry/', views.contactEnquiry, name = 'enquiry'),
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.login_view, name='login'),
    path('logout,', views.logout, name = 'logout')

    
]