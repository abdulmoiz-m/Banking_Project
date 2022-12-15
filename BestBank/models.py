from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
