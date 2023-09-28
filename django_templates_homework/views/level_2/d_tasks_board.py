"""
Оживите шаблон.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def tasks_board_view(request: HttpRequest) -> HttpResponse:
    title = 'Tasks'
    tasks = [
        {"title": "Помыть посуду", "status": "in_progress"},
        {"title": "Вымыть пол", "status": "todo"},
        {"title": "Выспаться", "status": "done"},
        {"title": "Посмотреть кино", "status": "done"},
        {"title": "Застелить кровать", "status": "in_progress"},
        {"title": "Купить продуктов", "status": "todo"},
    ]
    return render(request, 'level_2/tasks_board.html', context={"title": title, "tasks": tasks})
