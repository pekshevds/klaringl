from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    comment = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        abstract = True


class DirectorySerializer(BaseSerializer):
    name = serializers.CharField()

    class Meta:
        abstract = True
