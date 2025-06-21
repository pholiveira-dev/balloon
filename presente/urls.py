from . import views
from django.urls import path

app_name = 'presente'

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhe_produto/<int:id>/', views.produtos, name='detalhe_produto'),
    path('produtos/', views.todos_produtos, name='lista'),
    path('categoria/<slug:slug>/', views.categoria, name='categoria'),
]

