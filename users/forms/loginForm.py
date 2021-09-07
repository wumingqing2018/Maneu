from captcha.fields import CaptchaField
from django import forms
from django.core.validators import RegexValidator
from django.forms import widgets


class LoginForm(forms.Form):

    username = forms.CharField(label="账号",
                               required=True,
                               strip=True,
                               widget=widgets.TextInput(
                                   attrs={'id': 'username', 'class': 'form-control', 'placeholder': '账号'}
                               ),
                               validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '只支持数字和字母')],
                               error_messages={'required': '请输入账号'},
                               )

    password = forms.CharField(label="密码",
                               required=True,
                               strip=True,
                               widget=widgets.TextInput(
                                   attrs={'id': 'password', 'class': 'form-control', 'placeholder': '密码'}
                               ),
                               validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '只支持数字和字母')],
                               error_messages={'required': '请输入密码'},
                               )

    captcha = CaptchaField(label="验证码",
                           required=True,
                           error_messages={"required": "验证码不能为空",
                                           "invalid": "验证码错误"}
                           )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username != 'unlock' and password != 'XMacheNike':
            raise forms.ValidationError('登录失败')
