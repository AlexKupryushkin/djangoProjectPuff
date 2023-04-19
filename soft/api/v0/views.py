from rest_framework import viewsets, pagination

from .serializers import DivanSerializer, OrderSerializer
from ...models import Divan, Orders


class DivanPaginator(pagination.PageNumberPagination):
    page_size = 3


class DivanControlViewSet(viewsets.ModelViewSet):
    queryset = Divan.objects.all()
    serializer_class = DivanSerializer
    # lookup_url_kwarg = "pizza_id"
    # pagination_class = DivanSerializer

    def get_queryset(self):
        queryset = Divan.objects.all()

        # if self.request.query_params.get("hot"):
        #     queryset = queryset.filter(hot=True)
        # if self.request.query_params.get("vegan"):
        #     queryset = queryset.filter(vegan=True)
        return queryset


class OrderControlViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "order_id"