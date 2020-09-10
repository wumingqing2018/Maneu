from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator


class SearchForm(forms.Form):

    order_id = forms.IntegerField(label="订单号",
                                  required=False,
                                  strip=True,
                                  initial='1',
                                  widget=widgets.TextInput(
                                      attrs={'id': 'from_order_id', 'placeholder': '订单号'}
                                  ),
                                  error_messages={'required': '请输入id'},
                                  )
