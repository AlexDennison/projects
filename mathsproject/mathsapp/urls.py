from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.addition,name='add'),
    path('subtract/',views.subtraction,name='sub'),
    path('multiply/',views.multiplication,name='mul'),
    path('divide/',views.division,name='div'),
    path('mod/',views.remainder,name='rem'),
]