# api/utils.py
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions

def create_jwt_for_user(user):
    payload = {"id": str(user.id), "email": user.email}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    # jwt.encode returns str in PyJWT>=2
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION", "")
        if not auth:
            return None
        parts = auth.split()
        if len(parts) != 2:
            return None
        prefix, token = parts
        if prefix.lower() != "bearer":
            return None
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token expired")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed("Invalid token")
        try:
            user = User.objects.get(id=payload.get("id"))
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        return (user, None)
