import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit


this_dir = pathlib.Path(__file__).resolve().parent

def home_page(request, *args, **kwargs):
    page_visits_count = PageVisit.objects.count()
    
    my_title = "Hello there..."
    my_context = {"page_title": my_title, "page_visits_count": page_visits_count}
    
    PageVisit.objects.create(path=request.path)
    
    return render(request, "home.html", my_context)