from datetime import timedelta

from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

TIMEOUT_SECONDS = 60


class ExpirationTokenAuthentication(TokenAuthentication):
    delta = timedelta(seconds=TIMEOUT_SECONDS)

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid Token.")
        
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User is not active.")

        now = timezone.now()
        if now - token.created > self.delta:
            token.delete()
            raise exceptions.AuthenticationFailed("The Token is expired.")
        
        token.created = now
        token.save(update_fields=['created'])
        return (token.user, token)
