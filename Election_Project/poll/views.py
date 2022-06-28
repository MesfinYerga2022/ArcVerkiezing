from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll

def index(request):
    polls =  Poll.objects.all()
    context={
        'polls': polls
     }
    return render(request,'poll/index.html',context)
def home(request):
    polls =  Poll.objects.all()
    context={
        'polls': polls
     }
    return render(request,'poll/home.html',context)
def create(request):
    if request.method =='POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context={
        'form': form
    }
    return render(request,'poll/create.html',context)
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
         selected_option = request.POST['poll']
         if selected_option=='candidate1':
             poll.candidate_one_count +=1
         elif selected_option=='candidate2':
             poll.candidate_two_count +=1
         elif  selected_option=='candidate3':
             poll.candidate_three_count +=1
         else:
            return HTTPResponse(400,'Invalid form')
         poll.save()
         return redirect('results',poll.id)
    context = {
        'poll' : poll
    }
    return render(request,'poll/vote.html',context)
def results(request, poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context={
        'poll' : poll
     }
    return render(request,'poll/results.html',context)

