from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
    path('crops/', views.crops_index, name='index'),
    path('crops/<int:crop_id>/', views.crops_detail, name='detail'),
 ]