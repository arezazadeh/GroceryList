from django.views.decorators.http import require_GET
from django.shortcuts import render
from django.contrib.auth.models import User
from notifications.signals import notify


def home(request):
    return render(request, 'home.html')

def message(request):
    users = User.objects.all()
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        sender = User.objects.get(username=request.user)
        receiver = User.objects.get(id=request.POST.get('user_id'))
        notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
        return render(request, "push.html", {'users': users, 'user': user})
    
    return render(request, "push.html", {'users': users, 'user': user}) 