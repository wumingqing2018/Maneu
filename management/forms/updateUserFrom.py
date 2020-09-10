from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    user_name = forms.CharField(label="姓名",
                                required=True,
                                strip=True,
                                widget=widgets.TextInput(
                                    attrs={'class': 'form_user_account', 'placeholder': '姓名'}
                                ),
                                validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '不能输入特殊字符')],
                                error_messages={'required': '请输入姓名'},
                                )

    user_account = forms.CharField(label="账号",
                                   required=True,
                                   strip=True,
                                   widget=widgets.TextInput(
                                       attrs={'class': 'form_user_account', 'placeholder': '账号'}
                                   ),
                                   validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '不能输入特殊字符')],
                                   error_messages={'required': '请输入账号'},
                                   )

    user_password = forms.CharField(label="密码",
                                    required=True,
                                    strip=True,
                                    widget=widgets.TextInput(
                                        attrs={'class': 'form_user_password', 'placeholder': '密码'}
                                    ),
                                    validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '不能输入特殊字符')],
                                    error_messages={'required': '请输入密码'},
                                    )

    valid_time = forms.DateField(label="有效时间",
                                 required=True,
                                 strip=True,
                                 widget=widgets.TextInput(
                                     attrs={'class': 'form_user_password', 'placeholder': '密码'}
                                 ),
                                 validators=[RegexValidator(r'^[A-Za-z0-9_]+$', '不能输入特殊字符')],
                                 error_messages={'required': '请输入密码'},
                                 )
