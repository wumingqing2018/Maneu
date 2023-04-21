import json

from django.shortcuts import render, HttpResponseRedirect, reverse

from common import common
from maneu_guest import service


def index(request):
    list = service.guess_all(admin_id=request.session.get('id'))
    return render(request, 'maneu_guest/index.html', {'list': list})


def detail(request):
    guess = service.guess_id(id=request.POST.get('id'))
    Subjective = service.subjectiverefraction_guessID(guessid=guess.id)
    if Subjective:
        subjectiverefraction = json.loads(Subjective.content)
    else:
        subjectiverefraction = {'OS_VA': 0.2, 'OS_SPH': 0, 'OS_CYL': 0, 'OS_AX': 0, 'OS_AK': 0, 'OS_AL': 16, 'OS_BCVA': 0, 'OS_AD': 0, 'OS_CCT': 0, 'OS_LT': 0, 'OS_VT': 0,
                                'OD_VA': 0.2, 'OD_SPH': 0, 'OD_CYL': 0, 'OD_AX': 0, 'OD_AK': 0, 'OD_AL': 16, 'OD_BCVA': 0, 'OD_AD': 0, 'OD_CCT': 0, 'OD_LT': 0, 'OD_VT': 0,
                                'remark': ''}
    try:
        clientAge = int(guess.age)
        if clientAge > 20:
            stand_ax = '24.0'
        else:
            data = ['16.2', '17.0', '17.7', '18.2', '18.7', '19.1', '19.6', '20.0', '20.3', '20.7', '21.1', '21.6',
                    '22.0', '22.4', '22.7', '23.0', '23.3', '23.5', '23.7', '23.8', '24.0', '24.0', ]
            stand_ax = data[clientAge - 1]
    except:
        stand_ax = '24.0'

    return render(request, 'maneu_guest/detail_pc.html', {'guess': guess,
                                                          'subjectiverefraction': subjectiverefraction,
                                                          'stand_ax': stand_ax,
                                                          'list_r': subjectiverefraction['OD_AL'],
                                                          'list_l': subjectiverefraction['OS_AL']})


def insert(request):
    today = common.today()
    if request.method == 'POST':
        ManeuGuess = service.guess_insert(time=today, contents=request.POST.get('Guess_information'), admin_id=request.session.get('id'))
        ManeuSubjectiveRefraction = service.subjectiverefraction_insert(guess_id=ManeuGuess.id, content=request.POST.get('Subjective_refraction'))
        return HttpResponseRedirect(reverse('maneu_guest:index'))
    return render(request, 'maneu_guest/insert.html', {'today': today})


def delete(request):
    if request.method == 'POST':
        service.guess_delete(id=request.POST.get('id'))
    return HttpResponseRedirect(reverse('maneu_guest:index'))


def update(request):
    if request.method == 'GET':
        guess = service.guess_id(id=request.GET.get('id'))
        Subjective = service.subjectiverefraction_id(id=guess.subjective_id)
        subjectiverefraction = json.loads(Subjective.content)
        return render(request, 'maneu_guest/update.html', {'guess': guess, 'Subjective': subjectiverefraction})
    if request.method == 'POST':
        id = service.guess_id(id=request.POST.get('id')).subjective_id
        guess = service.guess_update(id=request.POST.get('id'), content=request.POST.get('Guess_information'))
        Subjective = service.subjective_update(id=id, content=request.POST.get('Subjective_refraction'))
    return HttpResponseRedirect(reverse('maneu_guest:index'))


def search(request):
    """查找指定订单"""
    admin_id = request.session.get('id')
    text = request.GET.get('text')
    time = request.GET.get('time')
    if text:
        list = service.find_Guess_search(text=text, admin_id=admin_id)
        return render(request, 'maneu_guest/index.html', {'list': list})
    if time:
        list = service.find_Guess_time(time=time, admin_id=admin_id)
        return render(request, 'maneu_guest/index.html', {'list': list})
    else:
        return HttpResponseRedirect(reverse('maneu_guest:index'))


def order_list(request):
    list = service.find_ManeuOrderV2_guess_id(guess_id=request.POST.get('id'))
    return render(request, 'maneu_order_v2/index.html', {'list': list})
