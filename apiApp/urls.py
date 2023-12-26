from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.get_data, name = 'get-data'),
    path('data/new/', views.post_data, name = 'post-data'),
    path('data/<int:pk>/', views.get_data_detail, name = 'get_data_detail'),
    path('data/<int:pk>/edit/', views.put_data, name = 'put_data'),
    path('data/<int:pk>/delete/', views.delete_data, name = 'delete_data'),
]

