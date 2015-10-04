from django.db import models


class Place(models.Model):

	address = models.CharField(max_length=255)
	longitude = models.IntegerField(default=0)
	latitude = models.IntegerField(default=0)
