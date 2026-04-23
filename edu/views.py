from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm


# ---------------- AUTOR ----------------
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'edu/autor_list.html', {'autores': autores})


def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Autor'})


def autor_update(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Editar Autor'})


def autor_delete(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request, 'edu/confirm_delete.html', {'obj': autor, 'titulo': 'Excluir Autor'})


# ---------------- EDITORA ----------------
def editora_list(request):
    editoras = Editora.objects.all()
    return render(request, 'edu/editora_list.html', {'editoras': editoras})


def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editora_list')
    else:
        form = EditoraForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Editora'})


def editora_update(request, id):
    editora = get_object_or_404(Editora, id=id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('editora_list')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Editar Editora'})


def editora_delete(request, id):
    editora = get_object_or_404(Editora, id=id)
    if request.method == 'POST':
        editora.delete()
        return redirect('editora_list')
    return render(request, 'edu/confirm_delete.html', {'obj': editora, 'titulo': 'Excluir Editora'})


# ---------------- LIVRO ----------------
 
# def livro_list(request):
#    livros = Livro.objects.all()
#    return render(request, 'edu/livro_list.html', {'livros': livros})


def livro_list(request):
    livros_list = Livro.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    paginator = Paginator(livros_list, 10)  # 10 livros por página

    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.page(1)
    except EmptyPage:
        livros = paginator.page(paginator.num_pages)

    return render(request, 'edu/livro_list.html', {'livros': livros})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Livro'})


def livro_update(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Editar Livro'})


def livro_delete(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_list')
    return render(request, 'edu/confirm_delete.html', {'obj': livro, 'titulo': 'Excluir Livro'})


# ---------------- PUBLICA ----------------
def publica_list(request):
    publicacoes = Publica.objects.all()
    return render(request, 'edu/publica_list.html', {'publicacoes': publicacoes})


def publica_create(request):
    if request.method == 'POST':
        form = PublicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publica_list')
    else:
        form = PublicaForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Publicação'})


def publica_update(request, id):
    publicacao = get_object_or_404(Publica, id=id)
    if request.method == 'POST':
        form = PublicaForm(request.POST, instance=publicacao)
        if form.is_valid():
            form.save()
            return redirect('publica_list')
    else:
        form = PublicaForm(instance=publicacao)
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Editar Publicação'})


def publica_delete(request, id):
    publicacao = get_object_or_404(Publica, id=id)
    if request.method == 'POST':
        publicacao.delete()
        return redirect('publica_list')
    return render(request, 'edu/confirm_delete.html', {'obj': publicacao, 'titulo': 'Excluir Publicação'})