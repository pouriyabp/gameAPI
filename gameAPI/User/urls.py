from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.AuthAPI.as_view, name='sign_up'),
]
