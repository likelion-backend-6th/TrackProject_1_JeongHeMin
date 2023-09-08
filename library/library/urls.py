"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
import account.views as account
import services.views as services

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', account.MainLoginView.as_view(), name='login'),
    path('signup/', account.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', login_required(services.MainPageView.as_view(), login_url='/login'), name='main'),
    path('/loan/<int:book_id>', services.LoanSuccessView.as_view(), name='loan_success')

]