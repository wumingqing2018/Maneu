from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict

# 分页组件
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

# service 层
from management import service

# 二维码组件
import qrcode
from io import BytesIO

# from组件
from management.forms.addOrderForm import AddOrderForms
from management.forms.updateOrderForm import UpdateOrderForms
from .forms.checkOrderForm import CheckOrderForm

# Create your views here.


def order_list(request):
    """初始化容器"""
    item = {}
    """加载搜索表单"""
    form = CheckOrderForm()
    item['form'] = form
    """
    已借图书查询并展示到前端页面
    """
    all_order = service.find_one_order_with_data(u_time='2020-08-12')  # 获取借书表中所有的数据
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
    item['contacts'] = contacts
    return render(request, 'management/order_list.html', item)


def check_order(request):
    if request.method == "POST":
        form = CheckOrderForm(request.POST)
        if form.is_valid():
            HttpResponse(form)
        else:
            print(form.errors)
            return render(request, 'management/order_list.html', {'form': form})


def add_order(request):
    if request.method == "POST":
        ret = {'status': True, 'error': None, 'data': None}
        form = AddOrderForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
            ret['status'] = False
            ret['data'] = form.errors
        return JsonResponse(ret)
    elif request.method == "GET":
        form = AddOrderForms()
        return render(request, 'management/add_order.html', {'form': form})


def update_order(request):
    if request.method == "POST":
        form = UpdateOrderForms(request.POST)
        if form.is_valid():
            print('成功')
            print(form.has_changed())
        else:
            print(form.errors)
        return render(request, 'management/update_order.html', {'form': form})
    elif request.method == "GET":
        order_id = request.GET['order_id']
        order = service.find_one_order_with_order_id(order_id)
        form = AddOrderForms(model_to_dict(order))
        return render(request, 'management/update_order.html', {'form': form})


def delete_order(request):
    if request.method == 'POST':
        try:
            order_id = request.POST['id']
            service.ProductManage.objects.filter(order_id=order_id).first().delete()
        except BaseException as msg:
            print(msg)
    else:
        return redirect('index')
        # order = ProductManage.objects.filter(id=id).first().delete()


def qr_code_api(request):
    if request.method == "GET":
        arg = request.GET['id'] + '/' + request.GET['token']
        url = 'http://172.20.10.6:8000/guest_find_order/'+arg
        img = qrcode.make(url)
        buf = BytesIO()
        img.save(buf)
        image_stream = buf.getvalue()
        return HttpResponse(image_stream, content_type='image/png')


def find_order(request, order_id, token):
    order = service.guest_find_order(order_id, token)
    return render(request, 'management/guest_order_page.html', {'order': order})


def ajax_test(request):
    if request.method == 'GET':
        obj = CheckOrderForm()
        return render(request, 'test.html', {'obj': obj})
    else:
        ret = {'status': True, 'order_id': request.POST['order_id']}
        print(ret)
        obj = CheckOrderForm(request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            # return redirect('http://www.baidu.com')　　# 使用ajax提交，即使redirect，也不会跳转
            ret['status'] = 'true'
        else:
            # print(obj.errors)　　# obj.errors 是一个django.forms.utils.ErrorDict对象，继承自dict(字典)数据类型，默认是ul
            # obj.errors有很多方法 默认为as_ul() 还有 as_json() as_data() as_text()
            ret['message'] = obj.errors.as_text()
        return JsonResponse(ret)  # json.dumps() 只能对python中的基本数据类型进行处理

