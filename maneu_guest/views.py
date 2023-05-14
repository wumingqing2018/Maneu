from django.shortcuts import render, HttpResponseRedirect, reverse
from datetime import datetime
from common import common
from maneu_guest import service
import json


def search(request):
    """查找指定订单"""
    text = request.GET.get('text')
    time = request.GET.get('time')
    if text:
        list = service.ManeuGuess_search(admin_id=request.session.get('id'), text=text)
        return render(request, 'maneu_guest/index.html', {'list': list})
    if time:
        list = service.ManeuGuess_time(admin_id=request.session.get('id'), time=datetime.strptime(time, "%Y-%m-%d"))
        return render(request, 'maneu_guest/index.html', {'list': list})
    else:
        return HttpResponseRedirect(reverse('maneu_guest:index'))


def index(request):
    return render(request, 'maneu_guest/index.html', {'list': service.ManeuGuess_all(admin_id=request.session.get('id'))})


def detail(request):
    id = request.POST.get('guess_id')
    guess = service.ManeuGuess_id(admin_id=request.session.get('id'), id=id)
    vision = service.find_ManeuOrderV2_all(guess_id=guess.id)
    subjective = service.ManeuSubjectiveRefraction_all(guess_id=guess.id)
    stand_ax = '24.0'
    subjective_refraction = {'OS_VA': 0.2, 'OS_SPH': 0, 'OS_CYL': 0, 'OS_AX': 0, 'OS_AK': 0, 'OS_AL': 16, 'OS_BCVA': 0,
                             'OS_AD': 0, 'OS_CCT': 0, 'OS_LT': 0, 'OS_VT': 0,
                             'OD_VA': 0.2, 'OD_SPH': 0, 'OD_CYL':  0, 'OD_AX': 0, 'OD_AK': 0, 'OD_AL': 16, 'OD_BCVA': 0,
                             'OD_AD': 0, 'OD_CCT': 0, 'OD_LT': 0, 'OD_VT': 0,
                             'remark': ''}

    return render(request, 'maneu_guest/detail.html', {'guess': guess,
                                                       'vision': vision,
                                                       'subjective': subjective,
                                                       'subjectiverefraction': subjective_refraction,
                                                       'stand_ax': stand_ax})


def insert(request):
    if request.method == 'POST':
        ManeuGuess = service.ManeuGuess_insert(admin_id=request.session.get('id'),
                                               time=request.POST['time'],
                                               name=request.POST['name'],
                                               phone=request.POST['phone'],
                                               sex=request.POST['sex'],
                                               age=request.POST['age'],
                                               ot=request.POST['OT'],
                                               em=request.POST['EM'],
                                               dfh=request.POST['DFH'],
                                               remark=request.POST['remark'])
        request.POST._mutable = True
        request.POST['guess_id'] = ManeuGuess.id
        request.POST._mutable = False
        return detail(request)
    return render(request, 'maneu_guest/insert.html', {'today': common.today()})


def delete(request):
    service.ManeuGuess_delete(id=request.GET.get('guess_id'))
    return index(request)


def update(request):
    if request.method == 'POST':
        ManeuGuess = service.ManeuGuess_update(id=request.POST['guess_id'],
                                               time=request.POST['time'],
                                               name=request.POST['name'],
                                               phone=request.POST['phone'],
                                               sex=request.POST['sex'],
                                               age=request.POST['age'],
                                               ot=request.POST['OT'],
                                               em=request.POST['EM'],
                                               dfh=request.POST['DFH'],
                                               remark=request.POST['remark'])
        return detail(request)
    guess = service.ManeuGuess_id(admin_id=request.session.get('id'), id=request.GET.get('guess_id'))
    return render(request, 'maneu_guest/update.html', {'guess': guess})


def Subjective_detail(request):
    subjective = service.ManeuSubjectiveRefraction_id(id=request.POST.get('subjective_id'))
    return render(request, 'maneu_guest/subjective_detail.html', {'subjective': subjective, 'content': json.loads(subjective.content)})


def Subjective_delete(request):
    service.ManeuSubjectiveRefraction_delete(id=request.GET.get('subjective_id'), admin_id=request.session.get('id'))
    request.POST._mutable = True
    request.POST['guess_id'] = request.GET.get('guess_id')
    request.POST._mutable = False
    return detail(request)


def Subjective_insert(request):
    if request.method == 'POST':
        content = json.dumps(common.subjective_content(request))
        subjective_id = service.ManeuSubjectiveRefraction_insert(admin_id=request.session.get('id'), guess_id=request.POST.get('guess_id'), content=content).id
        request.POST._mutable = True
        request.POST['subjective_id'] = subjective_id
        request.POST._mutable = False
        return Subjective_detail(request)
    else:
        return render(request, 'maneu_guest/subjective_insert.html', {'guess_id': request.GET.get('guess_id')})


def Subjective_update(request):
    if request.method == 'POST':
        content = json.dumps(common.subjective_content(request))
        service.ManeuSubjectiveRefraction_update(id=request.POST['subjective_id'], admin_id=request.session.get('id'), content=content)
        return Subjective_detail(request)
    else:
        subjective = service.ManeuSubjectiveRefraction_id(id=request.GET.get('subjective_id'))
        return render(request, 'maneu_guest/subjective_update.html', {'subjective_id': subjective.id, 'content': json.loads(subjective.content)})
