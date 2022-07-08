from contextvars import Context
from http.client import HTTPResponse
from operator import concat
from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll

def index(request):
    polls =  Poll.objects.all()
    context={
        'polls': polls
     }
    return render(request,'poll/index.html',context)

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'poll/token.html')

@ms_identity_web.login_required
def home(request):
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/v1.0/users'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()
    polls =  Poll.objects.all()
    context_object_name = 'latest_question_list'

    context={
        'polls': polls
     }
    if 'value' in results:
        results ['num_results'] = len(results['value'])
        results['value'] = results['value'][:5]
    return render(request,'poll/home.html',context)
@ms_identity_web.login_required 
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


    #poll = Poll.objects.get(pk=poll_id)
    ##voters = [user.id for user in Voter.objects.filter(poll__id=poll_id)]
    #try:
    #    selected_choice = poll.choice_set.get(pk=request.POST['choice'])
       
    #except (KeyError, Choice.DoesNotExist):
    #    return render(request, 'poll/vote.html', {
    #        'poll': poll,
    #        #'error_message': "You didn't select a choice.",
    #    })
    #else:
    #    ##context = {
    #    ##'poll' : poll,
    #    ##            'error_message': "You didn't select a choice.",

    #    ##}

    #    selected_choice.votes += 1
    #    selected_choice.save()
    ##if request.method == 'POST':
    ##    #if request.user.id in voters:
    ##     selected_choice = request.POST['poll']
    ##     selected_choice.votes += 1
    ##     selected_choice.save()
    ##else:
    ##    return HTTPResponse(400,'Invalid form')
    ##    poll.save()
    ##    return redirect('results',poll.id)
   
    #    return redirect('results',poll.id)

    #back up
    # poll = Poll.objects.get(pk=poll_id)
    #try:
    #    selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    #    if selected_choice==poll.candidate:
    #        poll.candidate_count +=1

       
    #except (KeyError, Choice.DoesNotExist):
    #    return render(request, 'poll/vote.html', {
    #        'poll': poll,
    #    })
    #else:
    #     selected_choice.votes += 1
    #     poll.candidate_count +=1
    #     selected_choice.save()

    #     return redirect('results',poll.id)

    #end back up

def vote(request, poll_id):
       #poll = Poll.objects.get(pk=poll_id)
       #if request.method == 'POST':
       #     selected_option=request.POST['poll']
       #     if selected_option==poll.candidate:
       #      poll.candidate_count +=1
       #     #else:
       #     #     return HTTPResponse(400, 'invalid form')
       #     poll.save()
       #     return redirect('results',poll.id)

       #context = {
       #    'poll': poll
       # }
    
       #return render(request, 'poll/vote.html',context) 
    
     poll = Poll.objects.get(pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        if selected_choice==poll.candidate:
            poll.candidate_count +=1

       
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/vote.html', {
            'poll': poll,
        })
    else:
         selected_choice.votes += 1
         poll.candidate_count +=1
         selected_choice.save()

         return redirect('results',poll.id)





def results(request, poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context={
        'poll' : poll
     }
    return render(request,'poll/results.html',context)

def index(request):
    return render(request, "auth/status.html")

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')

@ms_identity_web.login_required
def call_ms_graph(request):
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/v1.0/users'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()

    # trim the results down to 5 and format them.
    if 'value' in results:
        results ['num_results'] = len(results['value'])
        results['value'] = results['value'][:5]

    return render(request, 'auth/call-graph.html', context=dict(results=results))


