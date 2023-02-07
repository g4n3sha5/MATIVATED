from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import TrainingSession, Technique, Suggestion, User
from .forms import TrainingSessionForm, addTechniqueForm, descriptionSuggestion
from django.core.paginator import Paginator
from django.contrib import messages
import json
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.


def BJJournalIndex(request):
    context = {
        'user': request.user
    }
    return render(request, "BJJournal/BJR_index.html", context)


def dashboard(request):
    context = {

    }

    return render(request, "BJJournal/BJR_dashboard.html", context)


def addSession(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, auto_id=True)

        if form.is_valid():
            sessionInstance = form.save(commit=False)
            messages.success(request, "Added your session")
            form.save()
            sessionInstance.addedByUser.add(request.user)
            return HttpResponseRedirect('/addSession')
        else:
            messages.error(request, "Invalid form. ")

    else:
        form = TrainingSessionForm()

    context = {
        'BJRform': form,
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_addSession.html", context)


def yourSessions(request):
    sessionsList = TrainingSession.objects.all().order_by('-date')
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    n = 3
    # sessions = None
    for index, item  in  enumerate(reversed(sessionsList), start=1):
        setattr(item, 'orderIndex', index)

    if is_ajax:
        data = json.load(request)
        size = data.get('device')
        if(size == 'small'):
            n = 3
        if(size == 'big'):
            n = 9

    p = Paginator(sessionsList, n)
    page = request.GET.get('page')
    sessions = p.get_page(page)

    form = TrainingSessionForm()

    context = {
        'BJRform': form,
        'sessionsList': sessions
    }
    # html = render_to_string('BJJournal/BJR_yourSessions.html', context)
    # return JsonResponse(html, safe=False)
    return render(request, "BJJournal/BJR_yourSessions.html", context)


def singleSessionView(request, id, orderIndex):
    print(orderIndex)
    Session = TrainingSession.objects.get(pk=id)
    context = {
        'session': Session,
        'orderIndex' : orderIndex,
        'form': TrainingSessionForm(instance=Session)
    }
    return render(request, "BJJournal/BJR_yourSessions/singleSessionView.html", context)


def editSession(request, id):

    Session = TrainingSession.objects.get(pk=id)

    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=Session, auto_id=True)

        if form.is_valid():
            form.save()

    return redirect ('/yourSessions')


def techniques(request):
    if request.method == 'POST':
        form = addTechniqueForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Added your technique")
            return redirect('/techniques')

        else:
            messages.error(request, "Invalid form. ")

    else:
        form = addTechniqueForm()

    context = {
        'TechForm': form,
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_Techniques.html", context)


def singleTechniqueView(request, id):
    techniqueObj = Technique.objects.get(pk=id)

    if request.method == 'POST':
        form = descriptionSuggestion(request.POST)

        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.technique_id = id
            suggestion.save()
            suggestion.addedByUser.add(request.user)

    else:
        form = descriptionSuggestion()

    UserSuggestions = request.user.suggestedByUser.all()
    userObjects = []

    for x in UserSuggestions:
        if x.technique_id == id:
            userObjects.append(Suggestion.objects.get(id=x.id))
        # userObjects.append(Suggestion.objects.get(id=x.id))
    context = {
        'technique': techniqueObj,
        'SuggestForm': form,
        'UserSuggestions': userObjects
    }
    return render(request, "BJJournal/BJR_Techniques/BJR_Techniques_singleTechniqueView.html", context)

# suggestion.techSuggestion.add(id)


# def addTechnique(request):
#     if request.method == 'POST':
#         form = addTechniqueForm(request.POST)
#         if form.is_valid():
#             tp = form.cleaned_data["type"]
#             leng = form.cleaned_data["length"]
#             dat = form.cleaned_data["date"]
#             loc = form.cleaned_data["location"]
#             # ts = TrainingSession(name=n)
#             # ts.save()
#             # t.user_lists.add(request.user)
#     #
#     # else:
#     #     form = TrainingSessionForm()
#
#     # context = {
#     #     'BJRform': form,
#     #     'techniquesList': Technique.objects.all()
#     # }
#     return render(request, "BJJournal/BJR_addSession.html", context)
