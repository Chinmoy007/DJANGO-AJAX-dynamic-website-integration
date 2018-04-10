
from django.conf.urls import url, include
from django.contrib import admin
from .  import views
urlpatterns = [
    url(r'^$', views.show_form, name = 'show_form'),
    
    # url(r'^signup/', views.signup, name = 'signup'),

]
