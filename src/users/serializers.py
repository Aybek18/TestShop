from rest_framework import serializers

from users.models import User


class UserLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(read_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password",)
