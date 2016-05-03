from django.db import models

# Create your models here.

class Address(models.Model):
	city = models.CharField(max_length=20)
	street = models.CharField(max_length=50)
	house = models.CharField(max_length=5)
	room = models.CharField(max_length=7)
	

	def __str__(self):
		return self.city

class Tarif(models.Model):
	tarif_name = models.CharField(max_length=30, blank=False)
	abonplata = models.PositiveIntegerField(blank=False)
	services = models.CharField(max_length=100)

class User(models.Model):
	contract = models.PositiveIntegerField(blank=False)
	abon_tarif = models.ManyToManyField(Tarif)
	first_name = models.CharField(max_length=30, blank=False)
	last_name = models.CharField(max_length=40, blank=False)
	phone_num = models.CharField(max_length=15, blank=True)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.first_name



#	"""docstring for User"""
#	def __init__(self, arg):
#		super(User, self).__init__()
#		self.arg = arg
		