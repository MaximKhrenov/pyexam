from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from shop_online.views import (ProductView, CategoryView, UserView, CartView, OrderView, HistoryView )

router = DefaultRouter()
router.register(r'product', ProductView)
router.register(r'category', CategoryView)
router.register(r'user', UserView, base_name='user')
router.register(r'cart', CartView)
router.register(r'history', HistoryView, base_name='history')
router.register(r'order', OrderView, base_name='order')
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]
