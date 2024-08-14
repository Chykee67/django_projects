from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = "latest"

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('id')[:3]
	

def PageTwo(request):
	page2 = "This is page two of my website".title()
	context = {
		"page2": page2
	}
	return render(request, "polls/page2.html", context)

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'



def Vote(request, ask_id):
	question = get_object_or_404(Question, pk=ask_id)

	if request.POST['choice']:
		try:
			selected_choice = question.choice_set.get(pk=request.POST['choice'])
		except(KeyError, Choice.DoesNotExist):
			return render(request, "polls/detail.html", {
				"question": question,
				"error message": "You did not select a choice.",
			})
		else:
			selected_choice.votes += 1
			selected_choice.save()

			return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
	else:
		return HttpResponseRedirect('polls: detail', args=(question.id))