from rest_framework import serializers
from brb.models import Away

class AwaySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    reason = serializers.CharField(max_length=512)
    creation_time = serializers.DateTimeField()
    return_time = serializers.DateTimeField(format="%H:%M")
    phone = serializers.BooleanField()
    active = serializers.BooleanField()



    
