from django.shortcuts import render

from maneu_admin import serivce


def user_list(request):
    return render(request, 'maneu_admin/index.html', {'user_list': serivce.find_user_all()})


def user_insert(request):
    if request.method == 'POST':
        if request.POST['gift_password'] == '214772680':
            updata = serivce.user_insert(username=request.POST['username'],
                                         nickname=request.POST['nickname'],
                                         password=request.POST['password'],
                                         phone=request.POST['phone'],
                                         email=request.POST['email'])
    return render(request, 'maneu_admin/insert.html')


def user_updata(request):
    admin_id = request.session.get('id')
    msg = ''
    if request.method == 'POST':
        updata = serivce.user_update(old_password=request.POST['old_password'], admin_id=admin_id,
                                     localtion=request.POST.get('localtion'),
                                     nickname=request.POST['nickname'], password=request.POST['password'],
                                     phone=request.POST['phone'], email=request.POST['email'],
                                     remark=request.POST['remark'])
        if updata:
            msg = '密码验证错误，请在密码验证输入正确的登录密码'
    user = serivce.find_user(admin_id)
    return render(request, 'maneu_admin/updata.html', {'maneu_admin': user, 'msg': msg})
