from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('logs/<int:file_id>/', views.view_logs, name='view_logs'),
    path('pass/<int:file_id>/', views.pass_file, name='pass_file'),
]