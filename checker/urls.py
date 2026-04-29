from django.urls import path
from . import views

urlpatterns = [
    path('', views.checker_view, name='checker'),
    path('history/', views.check_history, name='check_history'),
    path('detail/<int:check_id>/', views.check_detail, name='check_detail'),
]
