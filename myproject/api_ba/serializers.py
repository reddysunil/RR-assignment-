from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=['userid','id','title','body']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user