from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

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


def login(request):
    if request.method == 'GET':
        request.session['user'] = None
        form = LoginForm()
        return render(request, 'user/login_page.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = 'admin'
            return render(request, 'index_page.html')
        else:
            return render(request, 'user/login_page.html', {'form': form, 'error': '登录失败'})


def logout(request):
    request.session['user'] = None
    return render(request, 'index_page.html')


def join(request):
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


def list(request):
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
        if request.POST['id']:
            user = find_user(id=request.POST['id'])
            return render(request, 'user/page.html', {'user': user})
        return HttpResponse(request.POST)
    return render(request, 'error_page.html')
