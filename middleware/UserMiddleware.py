from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect


class LoginMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        print("--用户登录校验中间件启动--")

    def process_request(self, request):
        """
        产生request对象之后---url匹配之前调用
        判断用户是否登录
        白名单内app, 不需要登录
        用户没有登录, 跳转到登录页
        用户已经登录, 允许通过
        """
        login_url = '/user/login/'
        verify_list = ["order", "store"]
        request_url = request.path
        for verify in verify_list:
            if verify in request_url:
                try:
                    if request.session['user']:
                        return None
                except Exception as msg:
                    print(msg)
                return HttpResponseRedirect(login_url)
        return None
