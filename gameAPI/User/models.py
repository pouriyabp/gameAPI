from django.db import models

# Create your models here.


class SignUp(models.Model):
    Username = models.CharField(max_length=128, null=False, blank=False)
    TokenPublic = models.CharField(
        max_length=1024, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return f"User: {self.Username}"
