from .utils import code_generator , create_shortcode
from django.db import models
from django.conf import settings
from .validators import validate_url
#from django.core.urlresolvers import reverse 
from django_hosts.resolvers import reverse
#SHORTCODE_MAX = settings.SHORTCODE_MAX
SHORTCODE_MAX = getattr(settings , "SHORTCODE_MAX" , 15)

# Create your models here.

class winkURLManager(models.Manager):
	def all(self,*args , **kwargs):
		qs_main = super(winkURLManager, self).all(*args , **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self  , items=100):
		qs = winkURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items , int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes += 1
		return "new codes madde: {i}".format(i=new_codes)

class winkURL(models.Model):
	url = models.CharField(max_length=220 , validators=[validate_url])
	shortcode = models.CharField(max_length=SHORTCODE_MAX , unique=True , blank=True)
	updated = models.DateTimeField(auto_now=True) # everytime the model is save will set that value
	timestamp = models.DateTimeField(auto_now_add=True) # WHEN MODELS ARE CREATED
	active = models.BooleanField(default=True)
	objects = winkURLManager()

	def __str__(self):
		return str(self.url)
	
	def save(self ,*args, **kwargs):
		if self.shortcode is None or self.shortcode =="":
			self.shortcode = create_shortcode(self)
		super(winkURL, self).save(*args, **kwargs)

	def get_short_url(self):
		#url_path = reverse("scode" , kwargs={'shortcode':self.shortcode} , scheme="http")
		#return url_path
		return "wink1.heroku.com/{shortcode}".format(shortcode=self.shortcode)