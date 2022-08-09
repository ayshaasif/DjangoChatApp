from attr import field
from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ['id','image','first_name','last_name']


# class LoginSerializer(TokenObtainPairSerializer):
