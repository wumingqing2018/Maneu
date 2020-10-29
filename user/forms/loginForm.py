from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator


class LoginForm(forms.Form):

    username = forms.CharField(label="账号",
                               required=True,
                               strip=True,
                               widget=widgets.TextInput(
                                   attrs={'id': 'username', 'placeholder': '账号'}
                               ),
                               validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '只支持数字和字母')],
                               error_messages={'required': '请输入账号'},
                               )

    password = forms.CharField(label="密码",
                               required=True,
                               strip=True,
                               widget=widgets.TextInput(
                                   attrs={'id': 'password', 'placeholder': '密码'}
                               ),
                               validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '只支持数字和字母')],
                               error_messages={'required': '请输入密码'},
                               )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username != 'unlock' or password != 'XMacheNike':
            raise forms.ValidationError('登录失败')
