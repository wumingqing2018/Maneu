from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from users.server_redis import user_login_update
from users.server_redis import user_login_verify


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

        verify_list = ["order", "store", "users"]
        request_url = request.path
        session_key = request.session.session_key
        stats_login = user_login_verify(session_key)['users']

        for verify in verify_list:
            if verify in request_url:
                if stats_login:
                    user_login_update(session_key)
                else:
                    return redirect('login')
        user_login_update(session_key)
