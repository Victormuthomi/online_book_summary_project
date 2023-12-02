from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
	"""The home page for learning logs"""
	return render(request, 'learning_logs/index.xhtml')

@login_required
def topics(request):
	"""Show all the topics."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context={'topics': topics}
	return render(request, 'learning_logs/topics.xhtml', context)

@login_required
def topic(request, topic_id):
	"""Show a topic and all the enteries related to it."""
	topic = Topic.objects.get(id = topic_id)
	#make sure the topic belongs to the current user 
	if topic.owner != request.user:
		raise Http404
	
	enteries = topic.entry_set.order_by('added_date')
	context = {'topic':topic, 'enteries':enteries}
	return render(request, 'learning_logs/topic.xhtml', context)

@login_required
def new_topic(request):
	#add a new topic 
	if request.method != 'POST':
		#Its not a post request so return an empty form 
		form = TopicForm()
	else:
		#The user has entered data so you need to save 
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics')
	
	#display an invalid form  or blank form
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.xhtml', context)

@login_required
def new_entry(request, topic_id):
	"""Add a entry to a specific topic"""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		#Display a blank form
		form = EntryForm()
	else:
		#data submitted, validate and save
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id = topic_id)
	#display a blank or invalid form
	context = {'topic' : topic, 'form': form}
	return render(request, 'learning_logs/new_entry.xhtml', context)

 

@login_required
def edit_entry(request, entry_id,):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404
	
	if request.method != 'POST':
		#Display a blank form
		form = EntryForm(instance=entry)
	else:
		#data submitted, validate and save
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id = topic.id)
		
	#display a blank or invalid form
	context = {'entry': entry, 'topic' : topic, 'form': form }
	return render(request, 'learning_logs/edit_entry.xhtml', context)
	
	