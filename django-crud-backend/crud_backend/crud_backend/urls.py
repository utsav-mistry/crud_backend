from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, StudentViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)

router.register(r'students', StudentViewSet)

urlpatterns = [ 

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
