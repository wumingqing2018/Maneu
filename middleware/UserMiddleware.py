from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


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
        session_key = request.session.get('ip')
        request_url = request.path  # method:string, demo:/login/,
        #   判断是否需要校验字段
        if request_url.startswith('/maneu'):
            if session_key:
                #   判断用户是否登录
                if session_key:
                    return None
                else:
                    return redirect('login')
            else:
                return redirect('login')
        return None
