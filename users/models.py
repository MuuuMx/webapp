from django.db import models
from django.contrib.auth.models import User


class BusinessUser(models.Model):
	user = models.ForeignKey(User, default=8)
	businessname = models.CharField(max_length=140)
	type = models.CharField(max_length=140)
