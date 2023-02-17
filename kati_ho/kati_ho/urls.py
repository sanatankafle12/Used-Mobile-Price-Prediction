"""kati_ho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
""" from django.contrib import admin
from django.urls import path,include
from valuate import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('',views.homepage,name='home'),
    path('compare/',views.compare,name='compare'),
    path('valuate/',views.valuate,name='valuate'),
    path('sell/',views.sell_product,name='sell'),
    path('buy/',views.buy,name='buy'),
    path('recommend/',views.recommend,name='recommend'),
    path('logout/',views.logout,name='logout')
]

urlpatterns+=staticfiles_urlpatterns() """

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('valuate.urls')),
]