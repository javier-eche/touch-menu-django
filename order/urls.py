from django.urls import path
from .views import OrderCreateApi, OrderApi, OrderUpdateApi, OrderDeleteApi
urlpatterns = [
    path('', OrderApi.as_view()),
    path('create', OrderCreateApi.as_view()),
    path('<int:pk>', OrderUpdateApi.as_view()),
    path('<int:pk>/delete', OrderDeleteApi.as_view()),
]