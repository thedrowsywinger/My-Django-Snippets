from rest_framework import serializers

from drf_app.models import DRF_Model

class info_serializer(serializers.ModelSerializer):
    class Meta:
        model = DRF_Model
        fields = ('id','first_name', 'last_name', 'email')