from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='list'),
    path('update-task/<str:pk>',views.update,name='update'),
    path('delete-task/<str:pk>',views.delete,name='delete')
]