from django.shortcuts import render,HttpResponse
# from datetime import datetime
# from home.models import Contact
# from django.contrib import messages

# Create your views here.
def index(request):
    # context={
    #     'var'':"raja ji gye oil lene",
    # }
    # return HttpResponse("Index Baba")
    return render(request,'sat.txt')
