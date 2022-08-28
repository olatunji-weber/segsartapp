from django.shortcuts import render
from .models import ArtWork

# Create your views here.
artWork1, artWork2, artWork3 = ArtWork(), ArtWork(), ArtWork()
artWork1.name = "Kurumi Iragbiji"
artWork1.img = "img1.jpg"
artWork1.description = "Description coming from Django Framework backend"
artWork1.price = 550

artWork2.name = "Kurumi Iragbiji"
artWork2.img = "img2.jpg"
artWork2.description = "Django Framework backend holds Description 2"
artWork2.price = 950

artWork3.name = "Kurumi Iragbiji"
artWork3.img = "img3.jpg"
artWork3.description = "Description 3 coming from Django Framework backend"
artWork3.price = 1500

artWorks = [artWork1, artWork2, artWork3]


def index(request):
    return render(request, "index.html", {'artWorks': artWorks})

def gallery(request):
    return render(request, "gallery.html", {'artWorks': artWorks})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
