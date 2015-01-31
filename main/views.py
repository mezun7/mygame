import json
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
import operator
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin
from main.forms import LoginForm
from main.models import Team, Topic, Question
from main.structures.tableEntry import TableEntry


def get_sorted_teams_data():
    team_list = Team.objects.all()
    teams_score = {}

    for i in team_list:
        questions = i.question_set.all()
        sum = 0

        for j in questions:
            sum += j.score

        teams_score[i.name] = sum
    teams_score = sorted(teams_score.items(), key=operator.itemgetter(1), reverse=True)
    return teams_score
def get_topics_questions():
    topics_list = Topic.objects.all().order_by('name')
    list = []
    for i in topics_list:
        tmp = TableEntry(i.name, i.question_set.all().order_by('score'))
        list.append(tmp)
    return list



@login_required()
def index(request):

    teams_score = get_sorted_teams_data()
    topics_questions = get_topics_questions()
    #print teams_score
    return render(request, 'main/index.html', {"teams_sorted": teams_score, "topics_questions": topics_questions})


def log_out(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect(reverse("login"))


class LoginView(View, TemplateResponseMixin, FormMixin):
    template_name = 'main/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("home")
    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        return context
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(), **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(reverse('login'))

    def form_invalid(self, form):
        return self.get(self.request)

def test(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        city = request.POST['city']
        message = name + ' lives in ' + city

        return HttpResponse(json.dumps({'message': message})) #tried without the json. Doesn't work either

    return render(request, 'main/ajaxTest.html')
    #return render(request, 'main/test.html', {"s":"s"})

def stats(request):
    return HttpResponseRedirect(reverse("home"))
@login_required()
def get_question(request, qid):
    question = Question.objects.get(pk=qid)
    #print question
    teams = Team.objects.all().order_by('name')
    teams_score = get_sorted_teams_data()
    return render(request, 'main/question.html', {'question': question, 'teams': teams, 'sorted_teams': teams_score})
@login_required()
def score_answer(request, qid, tid):
    #print qid, tid

    question = Question.objects.get(pk=qid)
    if not question.team_answered:
        question.team_answered = Team.objects.get(pk=tid)
        question.used = True
        question.save()
    return HttpResponseRedirect(reverse("home"))