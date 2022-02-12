from rest_framework import serializers

from applications.store.models import Store, Visit


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=255, write_only=True)
    store_id = serializers.UUIDField(write_only=True)
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = Visit
        exclude = ("store",)

    def create(self, validated_data):
        store_id = validated_data.pop("store_id")
        phone_number = validated_data.pop("phone_number")
        try:
            store_object = Store.objects.get(id=store_id)
            validated_data["store"] = store_object
            if not store_object.worker.phone == phone_number:
                msg = f"Phone number mismatch for Store({store_id})."
                raise serializers.ValidationError(msg)

        except Store.DoesNotExist:
            msg = f"Invalid store id: {store_id}."
            raise serializers.ValidationError(msg)

        return super().create(validated_data)
