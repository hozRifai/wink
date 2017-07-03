import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings , "SHORTCODE_MIN" , 6) # 6 is an alternate value 


def code_generator(size=SHORTCODE_MIN , chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size)) # _  for loop 


def create_shortcode(instance , size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	klass = instance.__class__  #print(instance.__class__ )
	qs = klass.objects.filter(shortcode=new_code).exists()
	if qs:
		return create_shortcode(size=size)
	return new_code

