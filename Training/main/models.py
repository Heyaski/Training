from django.db import models
from django.utils import timezone

class AboutMePhoto(models.Model):
    photo_about_me = models.ImageField(upload_to='about_me_photo/', blank=True, null=True)  # Поле для загрузки изображения

    def __str__(self):
        return "Секция Обо мне"

class AboutMeInfo(models.Model):
    firstParagraph = models.TextField(null=True, blank=True)
    secondParagraph = models.TextField(null=True, blank=True)

    def __str__(self):  # Исправленный отступ
        return "text1"
    
class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)  # Установите значение по умолчанию

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=255)  # Название услуги
    duration = models.CharField(max_length=100)  # Длительность
    session_length = models.CharField(max_length=100)  # Длительность одной сессии
    format = models.CharField(max_length=100)  # Формат (например, онлайн)
    price = models.CharField(max_length=100)  # Цена
    description = models.TextField(blank=True, null=True)  # Описание
    installment_available = models.BooleanField(default=False)  # Есть ли рассрочка
    additional_info = models.TextField(blank=True, null=True)  # Дополнительная информация

    def __str__(self):
        return self.title
    
class GroupWork(models.Model):
    title = models.CharField(max_length=255)  # Название групповой работы
    duration = models.CharField(max_length=100)  # Длительность
    session_length = models.CharField(max_length=100)  # Длительность одной сессии
    format = models.CharField(max_length=100)  # Формат (например, онлайн)
    price = models.CharField(max_length=100)  # Цена
    description = models.TextField(blank=True, null=True)  # Описание
    installment_available = models.BooleanField(default=False)  # Возможность рассрочки

    def __str__(self):
        return self.title
    
class Review(models.Model):
    author = models.CharField(max_length=255)  # Имя автора отзыва
    text = models.TextField()  # Текст отзыва
    photo = models.ImageField(upload_to='review_photos/', blank=True, null=True)  # Фото отзыва (опционально)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.author
    
class Diploma(models.Model):
    title = models.CharField(max_length=255)  # Название диплома
    image = models.ImageField(upload_to='diplomas/')  # Изображение диплома
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.title
    
class LawyerInfo(models.Model):
    IPname = models.TextField(null=True, blank=True)
    InnInfo = models.CharField(max_length=25, null=True, blank=True)
    OgrnInfo = models.CharField(max_length=25, null=True, blank=True)
    Adress = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.email