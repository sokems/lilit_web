from django.http import HttpResponse
from django.shortcuts import render, redirect

menu = [
    {'title':'Администрирование', 'url_name': 'seller'},
    {'title':'Менеджмент', 'url_name': 'manag'},
    {'title':'Выйти', 'url_name': 'logout'},
]

def mainpage_index(request):
    if request: #проверка доступа
        context = {
            'title': 'Главная страница',
            'menu': menu,
        }
        return render(request, 'mainpage/index.html', context=context)
    else:
        return redirect('guest', permanent=True)

def logout_index(request):
    return HttpResponse('Выход')

def pageNotFound(requets, exception):
    return HttpResponse('Страница не найдена')

def аccessIsDenied(requets, exception):
    return HttpResponse('Доступ запрещен')

def serverError(request):
    return HttpResponse('Ошибка сервера')

def requestError(request, exception):
    return HttpResponse('Неверный запрос')
