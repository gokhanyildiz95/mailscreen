from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "number" : 10
    }
    return render(request,"index.html",context)