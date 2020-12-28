from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseForbidden
from surveys.models import Survey, Question, User, SurveyArea, Answer
import json


def surveys_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    surveys = Survey.objects.all()
    response_list = []
    for survey in surveys:
        response_list.append({'id': survey.id, 'survey name': survey.name, 'type' : survey.type})
    
    return JsonResponse({'data': response_list})

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
    question = Question(id=body['id'], content=body['content'], correct_answer=body['correct_answer'])
    question.save()
    return JsonResponse({'date': body})

def new_answer(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    body = json.loads(request.body)
    answer = Answer(id=body['id'], content=body['content'], question=body['question'])
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
        survey = Survey.objects.get(id=body['id'])
    except Survey.DoesNotExist:
        return HttpResponseNotFound('No such survey')
    if survey.author_id == body['author_id']:
        survey.delete()
    else:
        return HttpResponseForbidden()
    return JsonResponse({'date': survey.id})
