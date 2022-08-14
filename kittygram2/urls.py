from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cats.views import AchievementViewSet, CatViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'users', UserViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    #  Djoser создаст набор эндпоинтов - базовые,
    #  для управления пользователями в Django:
    path('auth/', include('djoser.urls.jwt')),
    #  JWT-эндпоинты, для управления JWT-токенами
]
