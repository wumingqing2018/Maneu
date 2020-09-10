from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator


class CheckOrderForm(forms.Form):

    id = forms.CharField(label="单号",
                         required=True,
                         widget=widgets.TextInput(
                             attrs={'id': 'search', 'placeholder': '单号'}
                         ),
                         validators=[RegexValidator(r'^[0-9]+$', '只支持数字和字母')],
                         error_messages={'request': '请输入单号'},
                         )
