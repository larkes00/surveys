from django.http import JsonResponse, HttpResponseNotAllowed


def surveys(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    return JsonResponse({'foo': 'bar'})
