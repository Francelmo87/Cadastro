from django.urls import path, include

from .views import views as v

app_name =  'pedido'


urlpatterns = [
    path('', v.pedido_list_all, name='pedido_list_all'),
]
