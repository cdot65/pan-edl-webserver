from rest_framework import serializers
from .models import EDLEntry


class EDLEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EDLEntry
        fields = "__all__"
