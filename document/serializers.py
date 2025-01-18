from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.Serializer):
    class Meta:
        model = Document
        fields = ["file"]

    def create(self, validated_data):
        return Document.objects.create(**validated_data)
