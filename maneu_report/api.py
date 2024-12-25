from django.forms import model_to_dict
from django.http import JsonResponse

from common.common import report_simple
from common.verify import is_uuid, is_date
from maneu.models import ManeuReport
from maneu_report import service


def index(request):
    admin_id = is_uuid(request.session.get('id'))
    start = is_date(request.GET.get('start'))
    end = is_date(request.GET.get('end'))

    if admin_id and start and end:
        try:
            data = service.report_index(admin_id, start, end).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def search(request):
    admin_id = is_uuid(request.session.get('id'))
    text = request.GET.get('text')
    if admin_id:
        try:
            data = service.report_search(text=text, admin_id=admin_id).values('id', 'name', 'phone', 'time', 'remark')
            content = {'status': True, 'message': '', 'data': list(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def delete(request):
    id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))

    if admin_id and id:
        try:
            data = service.report_delete(admin_id=admin_id, id=id)
            content = {'status': True, 'message': '', 'data': {}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def insert(request):
    admin_id = is_uuid(request.session.get('id'))
    guest_id = is_uuid(request.GET.get('guest_id'))

    if admin_id and guest_id:
        content = report_simple(request.GET.get('content'))
        try:
            report = service.report_insert(admin_id=admin_id,
                                           guest_id=guest_id,
                                           time=request.GET.get('time'),
                                           name=request.GET.get('name'),
                                           phone=request.GET.get('call'),
                                           remark=request.GET.get('remark'),
                                           content=content)
            content = {'status': True, 'message': '', 'data': {'id':report.id}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数1', 'data': {}}

    return JsonResponse(content)


def update(request):
    report_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))
    time = request.GET.get('time')
    if admin_id and report_id:
        try:
            guest_id = service.guest_insert(admin_id, name=request.GET.get('name'), phone=request.GET.get('phone'), time=time)[0].id
            if guest_id:
                content = report_simple(request.GET.get('content'))
                report = service.report_update(id=report_id,
                                               admin_id=admin_id,
                                               guest_id=guest_id,
                                               name=request.GET.get('name'),
                                               time=request.GET.get('time'),
                                               phone=request.GET.get('call'),
                                               remark=request.GET.get('remark'),
                                               content=content)
                if report:
                    content = {'status': True, 'message': '', 'data': {'id': report_id}}
                else:
                    content = {'status': False, 'message': '请输入正确的参数3', 'data': {}}
            else:
                content = {'status': False, 'message': '请输入正确的参数2', 'data': {}}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def detail(request):
    report_id = is_uuid(request.GET.get('id'))
    admin_id = is_uuid(request.session.get('id'))
    if admin_id and report_id:
        try:
            data = service.report_detail(id=report_id, admin_id=admin_id)
            content = {'status': True, 'message': '', 'data': model_to_dict(data)}
        except Exception as e:
            content = {'status': False, 'message': str(e), 'data': {}}
    else:
        content = {'status': False, 'message': '请输入正确的参数', 'data': {}}

    return JsonResponse(content)


def test(request):
    data = ManeuReport.objects.filter().all()
    for i in data:
        content = report_simple(i.content)
        ManeuReport.objects.filter(id=i.id).update(content=content)
    return JsonResponse('')
