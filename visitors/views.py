from django.shortcuts import render, redirect
from django.http import HttpResponse
from visitors.forms import VisitorForms
from .models import  visitorsmodel,loginmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def visitors(request, id=0):
    user = request.session['username']
    type = loginmodel.objects.get(id=user)
    if request.method == "GET":
        if id == 0:
            forms = VisitorForms()
        else:
            user = visitorsmodel.objects.get(pk=id)
            forms = VisitorForms(instance=user)
        return render(request, "visitors.html", {'forms': forms,'type':type})
    else:
        if id == 0:
            forms = VisitorForms(request.POST)
        else:
            user = visitorsmodel.objects.get(pk=id)
            forms = VisitorForms(request.POST, instance=user)
        if forms.is_valid():
            userid = request.session['username']
            current_user = loginmodel.objects.get(id=userid)
            instance1 = forms.save(commit=False)
            instance1.username_id = current_user.id
            instance1.save()
            forms.save()
        return redirect('visitor_info')


def visitor_info(request):
    context = {'obj': visitorsmodel.objects.all()}
    return render(request, "visitor_info.html", context)


def visitors_delete(request, id):
    user = visitorsmodel.objects.get(pk=id)
    user.delete()
    return redirect('visitor_info')