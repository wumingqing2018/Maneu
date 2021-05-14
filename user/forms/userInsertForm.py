from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator


class UserInsertForm(forms.Form):
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

    email = forms.EmailField(label="邮件",
                             required=True,
                             error_messages={'required': '请输入邮箱'},
                             )

    phone = forms.CharField(label="电话",
                            required=True,
                            error_messages={'required': '请输入电话'},
                            )

    level = forms.CharField(label="等级",
                            required=True,
                            error_messages={'required': '请输入等级'},
                            )

    state = forms.CharField(label="状态",
                            required=True,
                            error_messages={'required': '请输入状态'},
                            )
