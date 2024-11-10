import json

from django.shortcuts import render

from common.common import current_time,subjective_content
from maneu_guest.service import *


def index(request):
    return render(request, 'maneu_guest/index.html')


def insert(request):
    return render(request, 'maneu_guest/insert.html', {'time': current_time()})


def detail(request):
    return render(request, 'maneu_guest/detail.html',{'id': request.GET.get('id')})


def update(request):
    return render(request, 'maneu_guest/update.html', {'id': request.GET.get('id')})



def Subjective_detail(request):
    subjective = ManeuSubjectiveRefraction_id(id=request.POST.get('subjective_id'))
    return render(request, 'maneu_guest/subjective_detail.html',
                  {'subjective': subjective, 'content': json.loads(subjective.content)})


def Subjective_delete(request):
    ManeuSubjectiveRefraction_delete(id=request.GET.get('subjective_id'),
                                     admin_id=request.session.get('id'))
    request.POST._mutable = True
    request.POST['guess_id'] = request.GET.get('guess_id')
    request.POST._mutable = False
    return detail(request)


def Subjective_insert(request):
    if request.method == 'POST':
        content = json.dumps(subjective_content(request))
        subjective_id = ManeuSubjectiveRefraction_insert(admin_id=request.session.get('id'),
                                                         guess_id=request.POST.get('guess_id'),
                                                         time=current_time(),
                                                         content=content).id
        request.POST._mutable = True
        request.POST['subjective_id'] = subjective_id
        request.POST._mutable = False
        return Subjective_detail(request)
    else:
        return render(request, 'maneu_guest/subjective_insert.html', {'guess_id': request.GET.get('guess_id')})


def Subjective_update(request):
    if request.method == 'POST':
        content = json.dumps(subjective_content(request))
        ManeuSubjectiveRefraction_update(id=request.POST['subjective_id'],
                                         admin_id=request.session.get('id'),
                                         content=content)
        return Subjective_detail(request)
    else:
        subjective = ManeuSubjectiveRefraction_id(id=request.GET.get('subjective_id'))
        return render(request, 'maneu_guest/subjective_update.html',{'subjective_id': subjective.id, 'content': json.loads(subjective.content)})
