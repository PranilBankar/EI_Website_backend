# api/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from .utils import create_jwt_for_user
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("start_time")
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        user = request.user
        # deadline
        if event.registration_deadline and timezone.now() > event.registration_deadline:
            return Response({"detail": "Registration closed"}, status=status.HTTP_400_BAD_REQUEST)
        if event.capacity is not None and event.remaining_seats == 0:
            return Response({"detail": "Event full"}, status=status.HTTP_400_BAD_REQUEST)
        reg, created = Registration.objects.get_or_create(event=event, user=user)
        serializer = RegistrationSerializer(reg)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class RegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Registration.objects.all().order_by("-registered_at")
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

@api_view(["POST"])
def api_login(request):
    """
    { username, password } -> { token, user }
    """
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    token = create_jwt_for_user(user)
    return Response({"token": token, "user": UserSerializer(user).data})
