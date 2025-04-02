from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_and_convert_file, name='upload_file'),
    path('download/<str:file_type>/<int:file_id>/', views.download_converted_file, name='download_file'),

]