from django.urls import include, path

from . import views as v

app_name = 'usuarios'


titular_patterns = [
   path('delete/<int:pk>/', v.titular_delete, name='titular_delete'),
   path('edit/<int:pk>/', v.titular_edit, name='titular_edit'),
   path('detail/<int:pk>/', v.titular_detail, name='titular_detail'),
   path('add/', v.titular_add, name='titular_add'),
   path('', v.titular_list, name='titular_list'),
]


dependente_patterns = [
   path('<int:pk>/', v.dependente_list, name='dependente_list'),
]


endereco_patterns = [
   path('<int:pk>/', v.endereco_titular, name='endereco_titular'),
]


urlpatterns = [
   path('titular/', include(titular_patterns)),
   path('membro/', include(dependente_patterns)),
   path('endereco/', include(endereco_patterns)),
]