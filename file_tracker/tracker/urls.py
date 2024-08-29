# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),  # Home page to list files
    path('upload/', views.upload_file, name='upload_file'),  # Upload file
    path('pass/<int:file_id>/', views.pass_file, name='pass_file'),  # Pass file
    path('log/<int:file_id>/', views.file_log, name='file_log'),  # View file log
]
