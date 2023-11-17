from django.urls import path, include
from .views import DashBoard, CreateUserView

urlpatterns = [
    path('', DashBoard.as_view(), name='dashboard'),
    path('createuser/', CreateUserView.as_view(), name='createuser')
]
