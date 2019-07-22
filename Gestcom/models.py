from django.db import models
# Create your models here.
    #date = models.DateTimeField(default=timezone.now, 
    #                            verbose_name="Date de parution")
class Clients(models.Model):
    	
    	nom     = models.CharField(max_length=255)
    	prenom     = models.CharField(max_length=100)
    	adresse     = models.CharField(max_length=100)
    	telephone     = models.CharField(max_length=100)
    	photo    = models.ImageField()

    	def __str__(self):
	        return "{0}".format(self.nom,)

class Lunette(models.Model):
		
		types = models.CharField(max_length=255)
		photo = models.ImageField()

		def __str__(self):
			return "{0}".format(self.types)

class Commandes(models.Model):
		date_add = models.DateTimeField()
		clients = models.ForeignKey('Clients', related_name="Clients", on_delete=models.CASCADE)
		lunette = models.ForeignKey('Lunette', related_name="Lunette", on_delete=models.CASCADE)