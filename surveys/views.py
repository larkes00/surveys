from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseForbidden
from surveys.models import Session, Survey, Question, User, SurveyArea, Answer, SurveyQuestion, Session
import json
from django.shortcuts import render


def surveys_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    surveys = Survey.objects.all()
    users = User.objects.all()
    areas = SurveyArea.objects.all()

    return render(request, 'surveys/surveys_list.html', {'surveys': surveys})

def survey(request, survey_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    try:
        Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return HttpResponseNotFound('No such survey')
    survey = Survey.objects.get(id=survey_id)
    response_list = []
    response_list.append({'id': survey.id, 'survey name': survey.name, 'type' : survey.type})
    
    return JsonResponse({'date': response_list})


def user_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    users = User.objects.all()
    response_list = []
    for user in users:
        response_list.append({'id': user.id, 'user name': user.name})

    return JsonResponse({'data': response_list})

def question_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    questions = Question.objects.all()
    response_list = []
    for question in questions:
        response_list.append({'id': question.id, 'question name': question.content})

    return JsonResponse({'date': response_list})

# TODO: Переделать функцию в survey
def survey_question_list(request, survey_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    surveyquestions = SurveyQuestion.objects.filter(survey_id=survey_id)
    survey = Survey.objects.get(id=survey_id)

    return render(request, 'surveys/question_list.html', {'surveyquestions': surveyquestions, 'survey_id': survey_id})

def survey_areas_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    survey_areas = SurveyArea.objects.all()
    response_list = []
    for survey_area in survey_areas:
        response_list.append({'id': survey_area.id, 'question name': survey_area.name})

    return JsonResponse({'date': response_list})

def new_survey(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    survey = Survey(id=body['id'], author_id=body['author_id'], area_id=body['area_id'],name=body['name'],type=body['type'])
    survey.save()
    return JsonResponse({'date': body})
    
def new_user(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    user = User(id=body['id'], name=body['name'])
    user.save()
    return JsonResponse({'date': body})

def new_question(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    question = Question(id=body['id'], content=body['content'], correct_answer_id=body['correct_answer_id'])
    question.save()
    return JsonResponse({'date': body})

def new_answer(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    answer = Answer(id=body['id'], content=body['content'], question_id=body['question_id'])
    answer.save()
    return JsonResponse({'date': body})
    
def new_survey_area(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    survey_area = SurveyArea(id=body['id'], name=body['name'])
    survey_area.save()
    return JsonResponse({'date': body})

def del_survey(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    try:
        session = Session.objects.get(id=body['session_id'])
    except Session.DoesNotExist:
        return HttpResponseNotFound('No such session')
    try:
        survey = Survey.objects.get(id=body['id'])
    except Survey.DoesNotExist:
        return HttpResponseNotFound('No such survey')
    if survey.author_id == session.user_id:
        survey.delete()
        return JsonResponse({'date': survey.id})
    else:
        return HttpResponseForbidden()

def del_question(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    try:
        question = Question.objects.get(id=body['question_id'])
    except Question.DoesNotExist:
        return HttpResponseNotFound('No such question')
    try:
        survey = Survey.objects.get(id=body['survey_id'])
    except Survey.DoesNotExist:
        return HttpResponseNotFound('No such survey')
    try:
        survey_question = SurveyQuestion.objects.get(survey_id=survey.id, question_id=question.id)
    except SurveyQuestion.DoesNotExist:
        return HttpResponseNotFound('the question is not related to the survey')
    try:
        session = Session.objects.get(id=body['session_id'])
    except Session.DoesNotExist:
        return HttpResponseNotFound('User not login')
    if session.user_id == survey.author_id:
        question.delete()
        return JsonResponse({'date': question.id})
    else:
        return HttpResponseNotAllowed()

    
def del_answer(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    try:
        answer = Answer.objects.get(id=body['id'])
    except Question.DoesNotExist:
        return HttpResponseNotFound('No such answer')
    answer.delete()
    return JsonResponse({'date': answer.id})
    
def del_survey_area(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    try:
        surveyarea = SurveyArea.objects.get(id=body['id'])
    except Question.DoesNotExist:
        return HttpResponseNotFound('No such survey area')
    surveyarea.delete()
    return JsonResponse({'date': surveyarea.id})

def del_user(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    try:
        user = User.objects.get(id=body['id'])
    except Question.DoesNotExist:
        return HttpResponseNotFound('No such user')
    user.delete()
    return JsonResponse({'date': user.id})
    
def login(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    try:
        user = User.objects.get(login=body['login'])
    except User.DoesNotExist:
        return HttpResponseNotFound('No such user')
    if user.password == body['password']:
        try:
            session = Session.objects.get(user_id=user.id)
        except Session.DoesNotExist:
            session_list = Session.objects.all()
            session_id = 0
            for session in session_list:
                if session.id is not None:
                    session_id = session.id
                    session_list = Session(id=session_id+1, user_id=user.id)
                    session_list.save()
            return JsonResponse({'session_id': session_id})
        return JsonResponse({'session_id': session.id})
    else:
        return HttpResponseNotFound('Wrong password')
    
def singup(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    user = User.objects.get(login=body['login'])
    if user is not None:
        return HttpResponseNotFound('Such user exists')
    user = User(id=body['id'], name=body['name'], login=body['login'], password=body['password'])
    user.save()
    return JsonResponse({'date': body})