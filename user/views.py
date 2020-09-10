from django.shortcuts import HttpResponse
from django.shortcuts import render

# 当前APP文件
from .forms.loginForm import LoginForm
from .forms.joinForm import JoinForm
from .forms.checkUserForm import CheckUserForm
from .serivce import *

# 分页组件
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


# Create your views here.


def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login_page.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('ok')
        else:
            return render(request, 'user/login_page.html', {'form': form})


def user_join(request):
    if request.method == 'GET':
        form = JoinForm()
        return render(request, 'user/join_page.html', {'form': form})
    elif request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            try:
                add_user(post=request.POST)
                return HttpResponse('ok')
            except Exception as error_msg:
                return HttpResponse(error_msg)
        else:
            return render(request, 'user/join_page.html', {'form': form})


def user_list(request):
    """初始化容器"""
    item = {}
    """加载搜索表单"""
    form = CheckUserForm()
    item['form'] = form
    """
    已借图书查询并展示到前端页面
    """

    all_order = find_all_user()  # 获取借书表中所有的数据
    paginator = Paginator(all_order, 30)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    item['userList'] = contacts
    return render(request, 'user/list_page.html', item)


def check_user(request):
    if request.method == 'POST':
        if request.POST['user_id']:
            user = find_user(user_id=request.POST['user_id'])
            return render(request, 'user/user_page.html', {'user': user})
        return HttpResponse(request.POST)
    return render(request, 'error_page.html')
