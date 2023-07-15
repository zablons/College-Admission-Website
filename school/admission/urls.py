from django.urls import path
from admission import views


urlpatterns = [path('index', views.Index, name='index'),
               path('', views.Signup, name='register'),
               path('login/', views.Signin, name='login'),
               path('logout/', views.Signout, name='logout'),
               path('profile/', views.Upload, name='profile'),
               ]

