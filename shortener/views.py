from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View 
from .models import winkURL
from .forms import SubmitUrlForm

# Create your views here.

class HomeView(View):
	def get(self , request , shortcode=None , *args , **kwargs):
		form = SubmitUrlForm()
		context = {
			"title" : "wink.io",
			"form": form
		}
		return render(request , "shortener/home.html" , context)

	def post(self , request , shortcode=None , *args , **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {"form":form , "title":"wink.io"}
		template = "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj , created = winkURL.objects.get_or_create(url=new_url)
			context = {"object":obj, "created":created}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"
		return render(request , template , context )

class winkCBView(View):
	def get(self , request , shortcode=None , *args , **kwargs):
		obj = get_object_or_404(winkURL , shortcode=shortcode)
		return HttpResponseRedirect(obj.url)