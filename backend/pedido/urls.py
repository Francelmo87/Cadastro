from django.urls import path, include

from . import views as v

app_name = 'pedido'


visitar_patterns = [
   path('', v.pedido_visitar_list, name='pedido_visitar_list'),
]


abastecer_patterns = [
   path('', v.pedido_abastecer_list, name='pedido_abastecer_list'),
]

urlpatterns = [
   path('', v.pedido_list_all, name='pedido_list_all'),
   path('add/', v.pedido_add, name='pedido_add'),
   path('<int:pk>/', v.pedido_detail, name='pedido_detail'),

   path('visitar/', include(visitar_patterns)),
   path('abastecer/', include(abastecer_patterns)),
]
