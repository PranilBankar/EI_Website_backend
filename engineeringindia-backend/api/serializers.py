# api/serializers.py
from rest_framework import serializers
from .models import Event, Registration
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    remaining_seats = serializers.ReadOnlyField()
    class Meta:
        model = Event
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
