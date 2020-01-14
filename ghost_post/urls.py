from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from ghosting import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
