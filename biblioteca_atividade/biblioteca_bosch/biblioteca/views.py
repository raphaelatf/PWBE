from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

def livro_read(request):
    if request.method == 'POST':
        livro = busca_livros(request)
    else:
        livro = [ ]
    livros = Livro.objects.all()
    return render(request, 'livro_read.html', {'livros' : livros, 'livro': livro})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else: 
        form = LivroForm()
    return render(request, 'biblioteca_form.html', {'form':form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'biblioteca_form.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_read')
    return render(request, 'confirmar_delete.html', {'livro': livro})

def busca_livros(request):
    informacao_busca = request.POST.get('info_livro')
    print(informacao_busca)
    livro = Livro.objects.filter(ano__icontains = informacao_busca) | Livro.objects.filter(autor__icontains = informacao_busca) | Livro.objects.filter(titulo__icontains = informacao_busca)
    return livro
