from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.db.models import QuerySet
from django.core.validators import MinLengthValidator

from . import constants as cons


class User(AbstractUser):

    username_error_message = {
            "unique": "A user with that username already exists.",
            "don't exists": "There is no user with this username"
        }

    username = models.CharField(
        max_length=cons.USERNAME_LENGTH_MAX,
        unique=True,
        help_text=f"Required. {cons.USERNAME_LENGTH_MAX} characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[UnicodeUsernameValidator(), MinLengthValidator(cons.USERNAME_LENGTH_MIN)],
        error_messages=username_error_message,
    )
    email = models.EmailField(
        unique=True,
        help_text="Enter a valid email address",
        validators=[EmailValidator()],
        )
    avatar = models.ImageField(blank=True, upload_to=cons.UPLOAD_USERS_AVATARS,)
    created_on = models.DateTimeField(auto_now_add=True,)
    update_on = models.DateTimeField(auto_now=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return f"Username: {self.username}, Email: {self.email}"
