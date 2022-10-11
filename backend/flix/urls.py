from django.urls import path
from . import views

urlpatterns = [

    path('', views.getMovies, name='movies'),
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('profile/', views.UserView.as_view()),
    path('logout/', views.LogoutView.as_view()),


]
