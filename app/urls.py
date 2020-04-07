from django.urls import path
from .views import *

urlpatterns = [
    # path('upload/', summary, name='upload'),
    path('display/', summary, name='display'),
    path('delete/', delete_files, name='delete'),
    path('regenerate/', regenerate, name='regenerate'),
    path('download/', download, name='download'),
]