from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from surveys.models import Survey, Question, User, SurveyArea


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
    surveys = Survey.objects.all()
    for survey in surveys:
        if survey_id == survey.id:
            return JsonResponse({'date': {'id': survey.id, 'survey name': survey.name, 'type' : survey.type}})

    return HttpResponseNotFound('No such survey')

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