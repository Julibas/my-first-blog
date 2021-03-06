from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)
def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)


def home(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	info_user = Question.objects.order_by('pub_date')
	template = loader.get_template('polls/base.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list})
	respprint = HttpResponse(template.render(context))
	print(respprint)
	return HttpResponse(template.render(context))



#def home(request):
#	return render(request, 'polls/home.html')