from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField( max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nome_cliente = models.CharField("Nome do cliente", max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_cliente
    