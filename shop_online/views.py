from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins
from shop_online.models import (Product, Category, User, Cart, Order)
from rest_framework.permissions import IsAuthenticated
from shop_online.serializers import (
    ProductSerializers,
    CategorySerializers,
    UserSerializers,
    CartSerializers,
    OrderSerializers,
    HistorySerializers,
)


class ProductView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  # mixins.CreateModelMixin,
                  ):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class CategoryView(GenericViewSet,
                   mixins.ListModelMixin,
                   # mixins.CreateModelMixin,
                   ):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class UserView(GenericViewSet,
               mixins.ListModelMixin,
               ):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializers
    queryset = User.objects.all()


class CartView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin, ):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializers
    queryset = Cart.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = OrderSerializers

    # queryset = Order.objects.all()
    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HistoryView(GenericViewSet,
    mixins.ListModelMixin):
    serializer_class = HistorySerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        username = self.request.user

        queryset = Order.objects.filter(user=username)
        return queryset