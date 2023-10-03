"""
Оживите шаблон.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def tasks_board_view(request: HttpRequest) -> HttpResponse:
    tasks = [
        {"title": "Помыть посуду", "status": "in_progress"},
        {"title": "Вымыть пол", "status": "todo"},
        {"title": "Выспаться", "status": "done"},
        {"title": "Посмотреть кино", "status": "done"},
        {"title": "Застелить кровать", "status": "in_progress"},
        {"title": "Купить продуктов", "status": "todo"},
    ]
    task_statuses = set(n["status"] for n in tasks)
    grouped_tasks_by_status = [(task_status, [task['title']\
                                for task in tasks if task['status'] == task_status])\
                                for task_status in task_statuses]
    return render(request, 'level_2/tasks_board.html', context={"tasks": grouped_tasks_by_status})
