"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import ProductViewSet, FashionViewSet, SportsViewSet, ElectronicsViewSet


# Created a router for managing API endpoints
router = routers.SimpleRouter()


router.register('products', ProductViewSet)         # API endpoint for products
router.register('fashion', FashionViewSet)          # API endpoint for fashion products
router.register('sports', SportsViewSet)            # API endpoint for sports products
router.register('electronics', ElectronicsViewSet)  # API endpoint for electronics products


urlpatterns = [
    path('', include(router.urls)),   # Included API endpoints defined by the router
    path('admin/', admin.site.urls),
]
