from django.shortcuts import render
from task1.models import Game


def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fourth_task/shop.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
