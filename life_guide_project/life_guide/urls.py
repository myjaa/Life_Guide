"""life_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from prevention import views as prevention_views 
from users import views as user_views
from chatbot import views as chatbot_views
from donate import views as donate_views
from shelter import views as shelter_views
from volunteer import views as volunteer_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',prevention_views.home,name='prevention'),
    path('register/',user_views.register, name='register'),
    path('chatbot/',chatbot_views.chatbot,name='chatbot'),
    path('donate/',donate_views.donate,name='donate'),
    path('shelter/',shelter_views.shelter,name='shelter'),
    path('volunteer/',volunteer_views.volunteer, name='volunteer'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
