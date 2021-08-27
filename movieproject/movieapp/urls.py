from django.urls import path

from movieapp import views

app_name = 'movieapp'

urlpatterns = [

    path('', views.index),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.addmov, name='addmov'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
