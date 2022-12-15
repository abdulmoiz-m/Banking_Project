from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Transactions(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False)
