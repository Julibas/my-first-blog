from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from .models import Address, Phone_book

# Create your views here.
def start(request):
	#linktodate = datetime.datetime.now()
	#data = HttpResponse.getvalue(self)
	all_data = Address.objects.all().values('city', 'street')

	return render_to_response('users/start.html', {'all_users': all_data})

@csrf_exempt
def work_data(request):
	if request.method == 'POST':
		some_data = request.POST
		f = some_data.get('contact_name')
		s = some_data.get('second_name')
		phone_num = some_data.get('phone_number')
		save_data = Phone_book(f_name=f, s_name=s, phone=phone_num)
		save_data.save()
		return render_to_response('users/start.html', {'linktodate': f})

@csrf_exempt
def all_contacts(request):
	if request.method == 'POST':
		all_phones = Phone_book.objects.all().values()
		return render_to_response('users/start.html', {'all_phones': all_phones})
