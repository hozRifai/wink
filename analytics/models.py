from django.db import models
from shortener.models import winkURL
# Create your models here.

class ClickEventManager(models.Manager):
	def create_event(self , wink_instance):
		if isinstance (wink_instance , winkURL ):
			obj = self.get_or_create(wink_url=wink_instance)
			obj.count +=1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	wink_url = models.OneToOneField(winkURL)
	#    wink_url    = models.OneToOneField(winkURL)

	count = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True) # everytime the model is save will set that value
	timestamp = models.DateTimeField(auto_now_add=True) # WHEN MODELS ARE CREATED 

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)