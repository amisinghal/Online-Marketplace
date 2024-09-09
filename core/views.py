from django.shortcuts import render

from item.models import Category, Item
# Create your views here.
# request= info about the browswer, ip address and the api request type get or post
# loading the templates/core here, templates are automatically located by django in the installed apps under settigns.py
def index(request):
    items= Item.objects.filter(is_sold=False)[0:6]
    categories= Category.objects.all()
    return render(request, 'core/index.html', {'categories':categories, 'items': items})

def contact(request):
    return render(request, 'core/contact.html')