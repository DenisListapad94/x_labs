import os


import jwt
from django.contrib.auth.base_user import (
    BaseUserManager,
    AbstractBaseUser,
)
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from dotenv import load_dotenv

load_dotenv()


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError("users must have username")
        if not email:
            raise TypeError("users must have email address")
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if not password:
            raise TypeError("superusers must have password")
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")

    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        db_index=True,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()

    def __str__(self):
        return f"{self.username} - {self.email}"

    def _generate_jwt_token(self):

        payload = {
            "id": self.pk,
            "username": self.username
        }

        return jwt.encode(payload, self.SECRET_KEY, algorithm=self.ALGORITHM)

    @property
    def token(self):
        return self._generate_jwt_token()

