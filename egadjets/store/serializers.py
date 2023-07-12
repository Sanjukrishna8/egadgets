from rest_framework import serializers
from .models import product
from django.contrib.auth.models import User

class productModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields="__all__"


    def validate(self, attrs):
        pr=attrs.get("price")
        if pr<0:
            raise serializers.ValidationError("invalid price count")
        return attrs
    

# django rest authentication   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
        