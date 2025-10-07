
from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('BMI/',views.BMI,name="BMI"),
    path('',views.BMI,name="BMI")
]