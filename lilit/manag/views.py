from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from mainpage.models import *
import mainpage.templates
from mainpage.views import menu
import json

def show_shops(id_user):
    shops = []
    user_list = SupUsers.objects.filter(id_user=id_user)
    if len(user_list) > 0:
        user_lk = json.loads(user_list[0].lk)
        for lk in user_lk:
            shop = AdminBots.objects.filter(name_bot=lk)[0]
            shops.append(shop)

    return shops

def manag_index(request):
    if request:  # проверка доступа
        shops = show_shops(395784406)
        context = {
            'title': 'Менеджмент',
            'menu': menu,
            'shops': shops,
            'shop_menu': [
                {'index': 'crm', 'title': 'CRM'},
                {'index': 'goods', 'title': 'Товары'},
                {'index': 'communication', 'title': 'Связь с магазином'},
            ]
        }

        return render(request, 'manag/main.html', context=context)
    else:
        return redirect('mainpage', permanent=True)

def crm_manag_index(request, name_bot):
    if request:  # проверка доступа
        shops = show_shops(395784406)
        bot = AdminBots.objects.filter(name_bot=name_bot)
        context = {
            'title': 'Менеджмент',
            'menu': menu,
            'shops': shops,
            'shop_menu': [
                {'index': 'crm', 'title': 'CRM'},
                {'index': 'goods', 'title': 'Товары'},
                {'index': 'communication', 'title': 'Связь с магазином'},
            ],
            'name_bot': bot[0],
            'crm_menu': [
                {'index': 'requests', 'title': 'Непринятые запросы'},
                {'index': 'myrequests', 'title': 'Личные запросы'},
            ]
        }

        return render(request, 'manag/crm.html', context=context)
    else:
        return redirect('mainpage', permanent=True)

def name_bot_manag_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        shops = show_shops(395784406)
        bit_list = AdminBots.objects.filter(name_bot=name_bot)[0]
        context = {
            'title': 'Менеджмент',
            'menu': menu,
            'shops': shops,
            'name_bot': name_bot,
            'bot': bit_list,
        }
        return render(request, 'manag/menu_shop.html', context=context)
    else:
        return redirect('mainpage', permanent=True)

def requests_manag_index(request, name_bot):
    if request:  # проверка доступа
        shops = show_shops(395784406)
        bot = AdminBots.objects.filter(name_bot=name_bot)
        list_reqs = SupReqs.objects.filter(status_req='Не принят', name_bot=name_bot)
        context = {
            'title': 'Менеджмент',
            'menu': menu,
            'shops': shops,
            'shop_menu': [
                {'index': 'crm', 'title': 'CRM'},
                {'index': 'goods', 'title': 'Товары'},
                {'index': 'communication', 'title': 'Связь с магазином'},
            ],
            'name_bot': bot[0],
            'list_reqs': list_reqs,
        }

        return render(request, 'manag/req.html', context=context)
    else:
        return redirect('mainpage', permanent=True)

def update_request(request, request_id):
    if request.method == 'POST':
        req = get_object_or_404(SupReqs, pk=request_id)
        req.status_req = 'Принят'  # Замените на нужное значение
        req.save()

        # Проверка, является ли запрос AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Запрос обновлен некорректно'})
    return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})

def myrequests_manag_index(request, name_bot):
    if request:  # проверка доступа
        return HttpResponse(f'Личные запросы от имени менеджера')
    else:
        return redirect('mainpage', permanent=True)

def communication_manag_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Связь с магазином <b>{name_bot}</b> от имени менеджера')
    else:
        return redirect('mainpage', permanent=True)

def goods_manag_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Товары в магазине <b>{name_bot}</b> от имени менеджера')
    else:
        return redirect('mainpage', permanent=True)

def add_goods_manag_index(request, name_bot):
    if len(AdminBots.objects.filter(pk=name_bot)) != 0 and name_bot: #проверка наличия магазина v проверка доступа
        return HttpResponse(f'Добавить товар в магазин <b>{name_bot}</b> от имени менеджера')
    else:
        return redirect('mainpage', permanent=True)


