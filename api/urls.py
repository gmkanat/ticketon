from api.views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('tickets', TicketViewSet, basename='tickets')
router.register('purchases', PurchaseViewSet, basename='purchases')
router.register('comments', CommentViewSet, basename='comments')
router.register('cities', CityViewSet, basename='cities')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls

