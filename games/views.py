from django.shortcuts import render, get_object_or_404
from .models import Games


# Create your views here.
def games(request):
    """Return the games.html file"""
    games = Games.objects.filter().order_by('name')
    return render(request, "games.html", {'games': games})


def games_detail(request, pk):
    """Create a view that returns a single Post object
    based on the post ID (pk) and render it  to the
    'postdetail.html' template. Or return a 404 error if
    the post is not found """
    games = get_object_or_404(Games, pk=pk)
    return render(request, "games_detail.html", {'games': games})
