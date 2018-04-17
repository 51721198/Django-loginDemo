"""LoginDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from login.views.login_views import SignUp, Login
from login.views.hospital_views import HospitalViews

sign = SignUp()
login = Login()
hospital = HospitalViews()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login.index),
    url(r'^login/', login.login),
    url(r'^sign-up/', sign.sign_up_index),
    url(r'^sign_up/', sign.signUp),
    url(r'^hospital/', hospital.getAllHospitals),
    url(r'^hospitalById/(.+)/$', hospital.getOneHospital)
]
