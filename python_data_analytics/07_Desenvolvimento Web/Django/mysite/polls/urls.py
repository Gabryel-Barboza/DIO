from django.urls import path

from . import views

# Nome da aplicação, impede ambiguidade ao referenciar métodos
app_name = 'polls'
# Rotas de polls, prefixo - método - identificador. Devem ser incluídos na configuração principal
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# Execute com ./manage.py runserver
