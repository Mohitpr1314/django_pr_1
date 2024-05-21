from django.contrib import admin






from .models import TourPackage, galleryphoto, SaveEnquiry
# Register your models here.

class Tour(admin.ModelAdmin):
    list_display = ('name', 'des', 'cost')
admin.site.register(TourPackage, Tour)

class Photo(admin.ModelAdmin):
    list_display = ('name', 'img')

admin.site.register(galleryphoto, Photo)



class Enquiry(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(SaveEnquiry, Enquiry)