from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# /api/v0/

# urlpatterns = [
#     path(
#         "pizza",
#         views.PizzaControlViewSet.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#             }
#         ),
#     ),
#     path(
#         "pizza/<int:pizza_id>",
#         views.PizzaControlViewSet.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#     ),
#     path(
#         "order",
#         views.OrderControlViewSet.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#             }
#         ),
#     ),
#     path(
#         "order/<int:order_id>",
#         views.OrderControlViewSet.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#     ),
# ]

router = DefaultRouter()

router.register("divans", views.DivanControlViewSet)
router.register("orders", views.OrderControlViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]