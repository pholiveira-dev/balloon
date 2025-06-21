from django.shortcuts import render
from .models import Produto, Categoria

def home(request):
    produtos = Produto.objects.all()[:3]
    categorias = Categoria.objects.all()
    return render(request, 'presente/pages/home.html', {
        'produtos': produtos,
        'categorias' : categorias
    })

def produtos(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'presente/pages/detalhe_produto.html', context={
        'produto' : produto
    })

def todos_produtos(request):
    produto = Produto.objects.all()
    return render(request, 'presente/pages/todos_produtos.html', context={
        'produtos': produto
    })

def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'presente/pages/categoria.html', context={
        'categoria': categoria,
        'produtos' : produtos
    })