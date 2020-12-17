from django.http import JsonResponse, HttpResponseNotAllowed
from surveys.models import Survey


def surveys_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    surveys = Survey.objects.all()
    response_list = []
    for survey in surveys:
        response_list.append({'id': survey.id})

    return JsonResponse({'data': response_list})
