from .views import LembreteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lembretes', LembreteViewSet, basename='lembrete')
urlpatterns = router.urls
