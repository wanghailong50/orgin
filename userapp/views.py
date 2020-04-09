from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def user_page(request):
    username=request.POST.get('username')
    print(username,11)
    return HttpResponse()