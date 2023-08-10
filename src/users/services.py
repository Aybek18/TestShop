from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class UserLoginService:
    @classmethod
    def login(cls, username: str, password: str) -> dict:
        existing_user = authenticate(username=username, password=password)
        if not existing_user:
            raise AuthenticationFailed()
        access_token, _ = Token.objects.get_or_create(user=existing_user)
        return {"access_token": access_token.key}
