from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect

class TestMiddleware(MiddlewareMixin):
    """中间件类"""

    def __init__(self, get_response):
        self.get_response = get_response
        print("--init--")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """url匹配之后---视图函数调用之前调用"""
        print("--process_view--")

    def process_response(self, request, response):
        """视图函数调用之后---内容返回浏览器之前"""
        print("--process_response--")
        return response
