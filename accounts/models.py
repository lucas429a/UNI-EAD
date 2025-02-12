from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(
        max_length=100,
        unique=True,
        error_messages={"unique": "user with this email already exists."}
    )
    is_superuser = models.BooleanField(default=False)
