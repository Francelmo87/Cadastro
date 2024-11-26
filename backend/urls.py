from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.base.urls')),
    path('usuarios/', include('backend.usuarios.urls')),
    path('pedidos/', include('backend.pedido.urls')),
]
