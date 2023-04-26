from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import DivanSerializer, OrderSerializer
from ...models import Divan, Orders


class DivanPaginator(pagination.PageNumberPagination):
    page_size = 3


class DivanControlViewSet(viewsets.ReadOnlyModelViewSet):
    """смотрим диваны"""

    queryset = Divan.objects.all()
    serializer_class = DivanSerializer
    pagination_class = DivanPaginator

    def get_queryset(self):
        queryset = Divan.objects.all()
        return queryset


class OrderControlViewSet(viewsets.ModelViewSet):
    """смотрим и создаем заказы"""

    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "order_id"
    permission_classes = (IsAuthenticatedOrReadOnly, )
