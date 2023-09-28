"""
В этом задании вам нужно оживить шаблон.

У вас уже есть готовая вьюха, которая пробрасывает нужный контекст и свёрстанная страница.
Проблема в том, что в шаблоне статичные данные, а нужно сделать так, чтобы шаблон использовал
данные из контекста и не содержал в себе "тестовых" данных. Этот процесс и называется оживлением.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django_templates_homework.custom_types import Message


def message_details_view(request: HttpRequest) -> HttpResponse:
    title = 'Детальная страница сообщения'
    message = Message(
        text='почувствуй себя ёжиком',
        author_nickname='bg yellow plum',
        likes_num=3,
        reposts_num=12,
    )
    return render(request, 'level_2/message_detail.html', context={"title": title, "message": message})
