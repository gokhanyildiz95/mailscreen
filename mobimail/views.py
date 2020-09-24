from django.shortcuts import render,HttpResponse

# Create your views here.
def new_mail(request,conversation_id,mail_id):
    context = {
        "number" : 10
    }
    return render(request,"new.html",context)

def view_conversation(request,conversation_id):
    print("conversation_id",conversation_id)
    context = {
        "number" : 10
    }
    return render(request,"view.html",context)