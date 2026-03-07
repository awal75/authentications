from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet,ProfileModelViewSet

router=DefaultRouter()
router.register('users',UserModelViewSet,basename='users')
router.register('profiles',ProfileModelViewSet,basename='profiles')


urlpatterns = router.urls
