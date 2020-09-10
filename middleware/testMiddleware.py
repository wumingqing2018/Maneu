from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect

class TestMiddleware(MiddlewareMixin):
    """中间件类"""

    def __init__(self, get_response):
        """服务器重启之后---接收第一个请求时调用"""
        self.get_response = get_response
        print("--init--")


    # def process_request(self, request):
    #     """产生request对象之后---url匹配之前调用"""
    #     if request.path == '/guest/' or request.path == '/':
    #         return None
    #         print(1)
    #     ticket = request.COOKIES.get('ticket')
    #     if ticket is None:
    #         return HttpResponseRedirect('/')
    #     return HttpResponseRedirect('/')


    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """url匹配之后---视图函数调用之前调用"""
        print("--process_view--")


    def process_response(self, request, response):
        """视图函数调用之后---内容返回浏览器之前"""
        print("--process_response--")
        return response
