import datetime

from django.db import models
from users.models import BusinessUser


class Place(models.Model):

	business_user = models.ForeignKey(BusinessUser)

	address = models.CharField(max_length=255)
	longitude = models.IntegerField(default=0)
	latitude = models.IntegerField(default=0)


class Product(models.Model):

	name = models.CharField(max_length=255)
	price = models.IntegerField()
	quantity = models.IntegerField()


#Insumos
class Material(models.Model):
	product = models.ForeignKey(Product)

	name = models.CharField(max_length=255)
	unity = models.CharField(max_length=255)
	quantity = models.IntegerField()
	cost = models.IntegerField()


class Sale(models.Model):
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	date = models.DateField(default=datetime.date.today)


# class Stock(models.Model):
# 	product = models.ForeignKey(Product)
# 	quantity = models.IntegerField()
