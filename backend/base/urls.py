from django.urls import path

from . import views as v

app_name = 'base'

urlpatterns = [
    path('', v.index, name='index'),
    path('login/', v.login_user, name='login'),
    path('logout/', v.logout_user, name='logout'),
]
