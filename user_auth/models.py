from django.db import models
from django.contrib.auth.models import AbstractUser


class BookUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - Admin: {self.is_admin} - Reviewer: {self.is_reviewer}"