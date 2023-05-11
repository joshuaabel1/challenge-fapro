from rest_framework import serializers

class UfValueSerializer(serializers.Serializer):
    date = serializers.CharField()
    uf_value = serializers.CharField()