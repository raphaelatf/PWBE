from django.shortcuts import render
from .models import Tarefa

def to_dolist(request):
    lista = Tarefa.objects.all().order_by('-data_criacao')
    return render(request, 'tarefas/lista_tarefa.html', {'lista':lista})   
