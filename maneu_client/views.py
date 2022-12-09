import json

from django.shortcuts import render, HttpResponseRedirect, reverse

from common.checkMobile import judge_pc_or_mobile
from maneu_client import service


def index(request):
    list = service.find_guess_list(user_id=request.session.get('id'))
    if list:
        return render(request, 'maneu_client/index.html', {'orderlist': list})
    else:
        orderlist = service.find_order_all(users_id=request.session.get('id'))  # 查找今日订单
        for order in orderlist:
            print(service.guess_update_userIdandId(user_id=order.users_id, id=order.guess_id))
            print(service.guess_update_subjective_id(subjective_id=order.subjectiverefraction_id, id=order.guess_id))

        list = service.find_guess_list(user_id=request.session.get('id'))
        return render(request, 'maneu_client/index.html', {'orderlist':list})



def detail(request):
    guess = service.find_guess_id(id=request.POST.get('id'))
    users = service.find_users_id(id=request.session.get('id'))
    Subjective = service.find_subjectiverefraction_id(id=guess.subjective_id)
    subjectiverefraction = json.loads(Subjective.content)
    try:
        clientAge = int(guess.age)
        if clientAge > 20:
            stand_ax = '24.0'
        else:
            data = ['16.2', '17.0', '17.7', '18.2', '18.7', '19.1', '19.6', '20.0', '20.3', '20.7', '21.1', '21.6',
                   '22.0', '22.4', '22.7', '23.0', '23.3', '23.5', '23.7', '23.8', '24.0', '24.0', ]
            stand_ax = data[clientAge-1]
    except:
        stand_ax = '24.0'

    ua = request.META.get("HTTP_USER_AGENT")
    mobile = judge_pc_or_mobile(ua)
    if mobile:
        return render(request, 'maneu_client/detail_phone.html', {'guess': guess, 'users': users, 'subjectiverefraction': subjectiverefraction, 'stand_ax': stand_ax, 'list_r': subjectiverefraction['OD_AL'], 'list_l': subjectiverefraction['OS_AL']})
    else:
        return render(request, 'maneu_client/detail_pc.html', {'guess': guess, 'users': users, 'subjectiverefraction': subjectiverefraction, 'stand_ax': stand_ax, 'list_r': subjectiverefraction['OD_AL'], 'list_l': subjectiverefraction['OS_AL']})


def insert(request):
    if request.method == 'POST':
        ManeuSubjectiveRefraction = service.ManeuSubjectiveRefraction_insert(content=request.POST.get('Subjective_refraction'))
        ManeuGuess_id = service.ManeuGuess_insert(content=request.POST.get('Guess_information'),
                                                  subjective_id=ManeuSubjectiveRefraction.id,
                                                  user_id=request.session.get('id'))
        return HttpResponseRedirect(reverse('maneu_client:index'))
    return render(request, 'maneu_client/insert.html')


def delete(request):
    if request.method == 'POST':
        service.guess_delete(id=request.POST.get('id'))
    return HttpResponseRedirect(reverse('maneu_client:index'))


def update(request):
    if request.method == 'GET':
        guess = service.find_guess_id(id=request.GET.get('id'))
        Subjective = service.find_subjectiverefraction_id(id=guess.subjective_id)
        subjectiverefraction = json.loads(Subjective.content)
        return render(request, 'maneu_client/update.html', {'guess': guess, 'Subjective': subjectiverefraction})
    if request.method == 'POST':
        id = service.find_guess_id(id=request.POST.get('id')).subjective_id
        guess = service.update_guess_id(id=request.POST.get('id'), content=request.POST.get('Guess_information'))
        Subjective = service.update_subjective_id(id=id, content=request.POST.get('Subjective_refraction'))
    return HttpResponseRedirect(reverse('maneu_client:index'))



def search(request):
    if request.method =='POST':
        """查找指定订单"""
        orderlist = service.find_ManeuGuess_search(date=request.POST.get('date'),
                                                   text=request.POST.get('text'),
                                                   users_id=request.session.get('id'))
        return render(request, 'maneu_client/index.html', {'orderlist': orderlist})
    else:
        return HttpResponseRedirect(reverse('maneu_client:index'))
