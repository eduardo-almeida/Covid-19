from django.urls import include, path
from . import views

urlpatterns = [
path('novo-usuario/', views.add_user, name='add_user'),
path('login-usuario/', views.user_login, name='user_login'),
path('logout-usuario/', views.logout_user, name='logout_user'),
]