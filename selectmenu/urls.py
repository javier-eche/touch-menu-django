from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/products/', include('product.urls')),
    path('api_generate_token/', views.obtain_auth_token),
]
