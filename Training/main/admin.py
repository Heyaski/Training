from django.contrib import admin
from .models import AboutMePhoto, AboutMeInfo, Publication, Service, GroupWork, Review, Diploma, LawyerInfo

@admin.register(AboutMePhoto)
class AboutMePhotoAdmin(admin.ModelAdmin):
    list_display = ['photo_about_me']
    
@admin.register(AboutMeInfo)
class AboutMeInfoAdmin(admin.ModelAdmin):
    list_display = ['firstParagraph', 'secondParagraph']
    
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']  # Исправлено на 'published_date'
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price', 'installment_available')
    
@admin.register(GroupWork)
class GroupWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price', 'installment_available')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')

@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    
@admin.register(LawyerInfo)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('IPname', 'InnInfo', 'OgrnInfo', 'Adress', 'email')