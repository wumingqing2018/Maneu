from django.http import JsonResponse

# Create your views here.
from rest_framework.views import APIView
from middleware.TestMiddleware import TokenAuth


#局部认证的配置
class Index(APIView):
    authentication_classes = [TokenAuth]

    def get(self, request):
        return JsonResponse({"index": "ok"})
