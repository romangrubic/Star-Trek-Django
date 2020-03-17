from django.shortcuts import render


# Create your views here.
def games(request):
    """Return the games.html file"""
    return render(request, "games.html")
