from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mainpage.models import *
import mainpage.templates
from mainpage.views import menu


def seller_index(request):
    if request:  # проверка доступа
        shops = AdminBots.objects.filter(own_user=395784406)
        return render(request, 'seller/main.html', {'title': 'Администрирование', 'menu': menu, 'shops': shops})
    else:
        return redirect('mainpage', permanent=True)

def name_bot_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Страница магазина <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)

def managers_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Менеджеры магазина <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)

def add_managers_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Добавить менеджера в магазин <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)

def communication_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Связь с магазином <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)

def goods_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Товары в магазине <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)

def add_goods_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Добавить товар в магазин <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)

def statistic_seller_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Статистика магазина <b>{name_bot}</b> от имени владельца')
    else:
        return redirect('mainpage', permanent=True)