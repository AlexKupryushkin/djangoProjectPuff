from rest_framework import serializers
from ...models import Divan, Orders


class DivanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divan
        fields = "__all__"

    # def to_representation(self, instance: Divan):
    #     res = super().to_representation(instance)
    #     res["cost"] = instance.diameters_cost
    #     return res


class OrderSerializer(serializers.ModelSerializer):
    divan_detail = DivanSerializer(source="divan", read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"
        # read_only_fields = ["cost"]