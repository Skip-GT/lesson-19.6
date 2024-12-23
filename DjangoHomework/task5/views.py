from django.shortcuts import render, HttpResponse
from .forms import UserRegister
from task1.models import Buyer
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, password=password, age=age, balance=0.00)
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['error'] = 'Некорректные данные'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})
