from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crops/', views.crops_index, name='index'),
    path('crops/<int:crop_id>/', views.crops_detail, name='detail'),
    path('crops/create/', views.CropCreate.as_view(), name='crops_create'),
    path('crops/<int:pk>/update/', views.CropUpdate.as_view(), name='crops_update'),
    path('crops/<int:pk>/delete/', views.CropDelete.as_view(), name='crops_delete'),
    path('crops/<int:crop_id>/add_reading/', views.add_reading, name='add_reading'),
] 