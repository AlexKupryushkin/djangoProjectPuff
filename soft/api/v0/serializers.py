from rest_framework import serializers
from ...models import Divan, Orders


class DivanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divan
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    divan_detail = DivanSerializer(source="divan", read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"
        # read_only_fields = ["cost"]
