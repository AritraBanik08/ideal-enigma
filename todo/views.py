from django.shortcuts import render
import database


def index(request):
    cur = database.conn()
    return render(request, 'main/index.html')