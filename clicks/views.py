from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'index.html', context)


def category(request):

    category = Category.objects.get()
    images = Image.objects.filter(category=category).order_by()[:6]
    
    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'category.html', context)


def imageDetail(request,):

    category = Category.objects.get()
    image = Image.objects.get()

    context = {}
    context['category'] = category
    context['image'] = image

    return render(request, 'image.html', context)

def search_results(request):

    if 'category' in request.GET and request.GET["categoty"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})




