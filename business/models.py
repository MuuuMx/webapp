from django.db import models
from users.models import BusinessUser


class Place(models.Model):

	business_user = models.ForeignKey(BusinessUser)

	address = models.CharField(max_length=255)
	longitude = models.IntegerField(default=0)
	latitude = models.IntegerField(default=0)
