from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('login', views.login, name='login'),
    path('user-authentication', views.user_authentication, name='login'),
    path('home', views.home, name='home'),
    path('list', views.list, name='list'),
    path('date-range', views.date_range, name='date_range'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
