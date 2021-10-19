from django.utils.deprecation import MiddlewareMixin


class FileMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response
        print("--excel文件校验中间件启动--")

    def process_request(self, request):
        """
        产生request对象之后---url匹配之前调用
        判断用户是否登录
        白名单内app, 不需要登录
        用户没有登录, 跳转到登录页
        用户已经登录, 允许通过
        """
        request_url = request.path  # method:string, demo:/login/,
        #   判断是否需要校验字段
        print(request_url)