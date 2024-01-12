from rest_framework import serializers

from ..models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=55,
        min_length=1,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

    def create(self, validated_data):
        return User.object.create_user(**validated_data)