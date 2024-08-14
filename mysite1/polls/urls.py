from django.urls import path
from . import views

app_name = "polls" #registers polls app in the namespace for use with templates

urlpatterns = [
    #polls/
	path("", views.IndexView.as_view(), name="index"),
    
	#polls/page2 - hard coding path - only "page2" will work
	path("page2", views.PageTwo, name="page2"),
    
	#polls/5/ - variably coding path, NUMBER can be any number, "5" or any other number would work the same
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
	#polls/5/results/ - 5 is variably coded, but "results" hard coded
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
	#polls/5/Vote/
    path("<int:ask_id>/vote/", views.Vote, name="vote"),
]
