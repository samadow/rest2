from django.urls import path

from .views import delete_user, get_user, update_user

urlpatterns = [
    path('', get_user, name='get_user'),
    path('update_user/<int:pk>/', update_user, name='update_user'),
    path('delete_user/<int:pk>/', delete_user, name='delete_user'),
]
