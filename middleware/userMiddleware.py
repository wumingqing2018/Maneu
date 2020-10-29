from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect

white_list = ['/guest/', '/user/']
login_url = '/user'


class UserMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        """服务器重启之后---接收第一个请求时调用"""
        self.get_response = get_response
        print("__init__")

    def process_request(self, request):
        """
        产生request对象之后---url匹配之前调用
        判断用户是否登录
        白名单内app, 不需要登录
        用户没有登录, 跳转到登录页
        用户已经登录, 允许通过
        """
        if request.path in white_list:
            return None

        try:
            ticket = request.session['user']
        except:
            request.session['user'] = None
            ticket = request.session['user']

        if ticket is None:
            return HttpResponseRedirect('/user')
        return None
