from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dogs/', views.dogs_index, name="index"),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name="dogs_create"),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('walkers/', views.WalkerList.as_view(), name='walker_index'),
    path('walkers/<int:pk>', views.WalkerDetail.as_view(), name="walker_detail"),
    path('walkers/create/', views.WalkerCreate.as_view(), name="walker_create"),
    path('walkers/<int:pk>/update/', views.WalkerUpdate.as_view(), name='walker_update'),
    path('walkers/<int:pk>/delete/', views.WalkerDelete.as_view(), name='toy_delete'),
    path('dogs/<int:dog_id>/add_visitors/', views.add_visitors, name='add_visitors'),
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
]