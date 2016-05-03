from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

# Create your views here.
def start(request):
	linktodate = datetime.datetime.now()
	#data = HttpResponse.getvalue(self)

	#print (data)
	return render_to_response('users/start.html')