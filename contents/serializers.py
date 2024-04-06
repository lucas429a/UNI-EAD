from rest_framework import serializers
from .models import Content


class ContentSerizalizer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = [
            "id",
            "name",
            "content",
            "video_url",
        ]

    def create(self, validated_data: dict) -> Content:
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
