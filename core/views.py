from django.shortcuts import render

# Create your views here.
# request= info about the browswer, ip address and the api request type get or post
# loading the templates/core here, templates are automatically located by django in the installed apps under settigns.py
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')