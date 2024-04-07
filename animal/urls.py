from django.urls import path
from animal.views import listar_animais, ver_animal

app_name = 'animais'
urlpatterns = [
    path('', listar_animais, name='listar_animais'),
    path('<int:id_animal>/', ver_animal, name='ver_animal')
]

