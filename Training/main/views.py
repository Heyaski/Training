from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutMePhoto, AboutMeInfo, Publication, Service, GroupWork, Review, Diploma, LawyerInfo


def show(request):
    data = {
        "about_me_photo": AboutMePhoto.objects.first(),
        "firstParagraph": AboutMeInfo.objects.first(),
        "secondParagraph": AboutMeInfo.objects.all()[1] if AboutMeInfo.objects.count() > 1 else None,
        "publications": Publication.objects.all(),  # Получаем все публикации
        "services": Service.objects.all(),
        "group_works": GroupWork.objects.all(),
        "reviews": Review.objects.all(),
        "diplomas": Diploma.objects.all(),
        "lawyerInfo": LawyerInfo.objects.first(),
    }

    return render(request, "index.html", data)
	



# def view_html_page(request):
#     if request.method == "GET":
#         data = {
#             "test": request.method
#         }

#         return render(request, "index.html", data)

#     if request.method == "POST":
#         data = {
#             "test": request.POST
#         }
#         return render(request, "index.html", data)

# def view_important_message(request):
#     return HttpResponse("""
#     <h1 style="color: red">КАКОГО ЧЁРТА?!?!?!?!?!?!?!</h1>
#     """)