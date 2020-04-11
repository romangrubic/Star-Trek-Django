from django.shortcuts import render, get_object_or_404
from .models import Games


# Create your views here.
def games(request):
    """Return the games.html file"""
    games = Games.objects.filter().order_by('id')
    return render(request, "games.html", {'games': games})


def games_detail(request, pk):
    """Create a view that returns a single Games object
    based on the game ID (pk) and render it  to the
    'games_detail.html' template. Or return a 404 error if
    the post is not found """
    games = get_object_or_404(Games, pk=pk)
    return render(request, "games_detail.html", {'games': games})
