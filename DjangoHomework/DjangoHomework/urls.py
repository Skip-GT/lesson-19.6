"""
URL configuration for DjangoHomework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task4 import views as app1
from task5 import views as app2
from task1 import views as app3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.index, name='index'),
    path('shop/', app1.shop, name='shop'),
    path('cart/', app1.cart, name='cart'),
    path('registration/', app2.sign_up_by_django, name='registration_page'),
    path('platform/news/', app3.news, name='news'),
]
