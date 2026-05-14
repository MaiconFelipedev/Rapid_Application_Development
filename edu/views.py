from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseNotAllowed
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm

def home(request):
    return redirect('livro_list')

# ---------------- AUTENTICAÇÃO ----------------

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'edu/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next' \
            '') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('home')
    else:
        form = SignInForm()

    return render(request, 'edu/signin.html', {'form': form})

def logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    logout(request)
    return redirect('signin')

# ---------------- AUTOR ----------------
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'edu/autor_list.html', {'autores': autores})

@login_required
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Autor'})

@login_required
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

@login_required
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

@login_required
def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editora_list')
    else:
        form = EditoraForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Editora'})

@login_required
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

@login_required
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

@permission_required('edu.add_livro', raise_exception=True)
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Livro'})

@permission_required('edu.change_livro', raise_exception=True)
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

@permission_required('edu.delete_livro', raise_exception=True)
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

@login_required
def publica_create(request):
    if request.method == 'POST':
        form = PublicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publica_list')
    else:
        form = PublicaForm()
    return render(request, 'edu/form.html', {'form': form, 'titulo': 'Cadastrar Publicação'})

@login_required
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

@login_required
def publica_delete(request, id):
    publicacao = get_object_or_404(Publica, id=id)
    if request.method == 'POST':
        publicacao.delete()
        return redirect('publica_list')
    return render(request, 'edu/confirm_delete.html', {'obj': publicacao, 'titulo': 'Excluir Publicação'})