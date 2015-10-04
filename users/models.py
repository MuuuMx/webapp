from django.db import models


class BusinessUser(models.Model):
	businessname = models.CharField(max_length=140)
	type = models.CharField(max_length=140)
