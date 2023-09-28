"""
Оживите шаблон.

Обратите внимание, что потенциально мошеннические транзакции подсвечиваются красным цветом в таблице.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django_templates_homework.generators.transactions import generate_fake_transactions


def transactions_list_view(request: HttpRequest) -> HttpResponse:
    title = 'Transactions'
    caption = 'transactions to review'
    num = 100
    transactions = generate_fake_transactions(num=num)
    return render(request, 'level_2/transactions_list.html', context={"title": title, "caption": caption, "num": num, "transactions": transactions})
