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
    path('crops/<int:crop_id>/add_photo/', views.add_photo, name='add_photo'),
    path('crops/<int:crop_id>/assoc_impact/<int:impact_id>/', views.assoc_impact, name='assoc_impact'),
    path('crops/<int:crop_id>/unassoc_impact/<int:impact_id>/', views.unassoc_impact, name='unassoc_impact'),
    path('impacts/', views.ImpactList.as_view(), name='impacts_index'),
    path('impacts/<int:pk>/', views.ImpactDetail.as_view(), name='impacts_detail'),
    path('impacts/create/', views.ImpactCreate.as_view(), name='impacts_create'),
    path('impacts/<int:pk>/update/', views.ImpactUpdate.as_view(), name='impacts_update'),
    path('impacts/<int:pk>/delete/', views.ImpactDelete.as_view(), name='impacts_delete'),
] 