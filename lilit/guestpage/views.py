from django.http import HttpResponse
from django.shortcuts import render

menu = ['Войти']
def guestpage_index(request):
    return render(request, 'guest/main.html', {'title': 'Гостевая страница', 'menu': menu})