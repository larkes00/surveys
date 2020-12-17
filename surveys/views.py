from django.http import JsonResponse

def list(request):
    print(request.body)
    if request.body:
        print("Post")
        return JsonResponse({'foo': 'bar'})
    
    raise ValueError