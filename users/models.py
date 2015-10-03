from django.db import models


class BaseUser(models.Model):
	username = models.CharField(max_length=140)
	password = models.CharField(max_length=140)
	email = models.CharField(max_length=140)

	def __unicode__(self):
		return self.username


class BusinessUser(models.Model):
	businessname = models.CharField(max_length=140)
	type = models.CharField(max_length=140)
