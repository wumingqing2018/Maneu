from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from test_jwt import views
urlpatterns = [
    # 登入验证，使用JWT的模块，只要用户密码正确会自动生成一个token返回
    url(r'^login/', obtain_jwt_token),
    # 访问需要认证的接口
    url(r'^index/', views.Index.as_view()),
]