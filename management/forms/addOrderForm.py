from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator


class AddOrderForms(forms.Form):
    c_name = forms.CharField(label='客户姓名',
                             required=True,
                             strip=True,
                             min_length=2,
                             max_length=10,
                             widget=widgets.TextInput(
                                 attrs={'id': 'c_name', 'placeholder': '客户姓名'}),
                             validators=[RegexValidator(r'^[\u4E00-\u9FA5A-Za-z0-9_]+$', '不能输入特殊字符')],
                             error_messages={'required': '请输入姓名', 'min_length': '格式不正确', 'max_length': '格式不正确'},
                             )
    c_phone = forms.CharField(label='客户电话',
                              required=True,
                              strip=True,
                              min_length=11,
                              max_length=11,
                              widget=widgets.TextInput(
                                  attrs={'id': 'c_phone', 'placeholder': '客户电话'}),
                              validators=[RegexValidator(r'1[1-9][0-9]{9}', '手机号格式不正确')],
                              error_messages={'required': '请输入电话'},
                              )
    l_glasses = forms.CharField(label="L_产品",
                                required=False,
                                strip=True,
                                max_length=20,
                                widget=widgets.TextInput(
                                    attrs={'id': 'l_glasses', 'placeholder': '产品'}),
                                validators=[RegexValidator(r'^[\u4E00-\u9FA5A-Za-z0-9_]+$', '不能输入特殊字符')],
                                error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                )
    l_sphere = forms.DecimalField(label="L_球镜",
                                  required=False,
                                  min_value=-24,
                                  max_value=16,
                                  max_digits=5,
                                  decimal_places=2,
                                  widget=widgets.TextInput(
                                      attrs={'id': 'l_sphere', 'placeholder': '球镜'}),
                                  error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                  )
    l_astigmatic = forms.DecimalField(label="L_散光",
                                      required=False,
                                      min_value=0,
                                      max_value=8,
                                      max_digits=5,
                                      decimal_places=2,
                                      widget=widgets.TextInput(
                                          attrs={'id': 'l_astigmatic', 'placeholder': '散光'}),
                                      error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                      )
    l_deviation = forms.IntegerField(label="L_偏位",
                                     required=False,
                                     min_value=0,
                                     max_value=180,
                                     widget=widgets.TextInput(
                                         attrs={'id': 'l_deviation', 'placeholder': '偏位'}),
                                     error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                     )
    l_add = forms.IntegerField(label="L_渐进",
                               required=False,
                               min_value=50,
                               max_value=400,
                               widget=widgets.TextInput(
                                   attrs={'id': 'l_add', 'placeholder': 'ADD'}),
                               error_messages={'min_value': '不能小于50', 'max_value': '不能超过500'},
                               )
    l_pd = forms.IntegerField(label="瞳距",
                              required=False,
                              min_value=43,
                              max_value=83,
                              widget=widgets.TextInput(
                                  attrs={'id': 'l_pd', 'placeholder': '瞳距'}),
                              error_messages={'min_value': '不能小于43', 'max_value': '不能超过83'},
                              )
    r_glasses = forms.CharField(label="R_产品",
                                required=False,
                                max_length=20,
                                widget=widgets.TextInput(
                                    attrs={'id': 'r_glasses', 'placeholder': '产品'}),
                                validators=[RegexValidator(r'^[\u4E00-\u9FA5A-Za-z0-9_]+$', '不能输入特殊字符')],
                                error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                )
    r_sphere = forms.DecimalField(label="R_球镜",
                                  required=False,
                                  min_value=-24,
                                  max_value=16,
                                  max_digits=5,
                                  decimal_places=2,
                                  widget=widgets.TextInput(
                                      attrs={'id': 'r_sphere', 'placeholder': '球镜'}),
                                  error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                  )
    r_astigmatic = forms.DecimalField(label="R_散光",
                                      required=False,
                                      min_value=0,
                                      max_value=8,
                                      max_digits=5,
                                      decimal_places=2,
                                      widget=widgets.TextInput(
                                          attrs={'id': 'r_astigmatic', 'placeholder': '散光'}),
                                      error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                      )
    r_deviation = forms.IntegerField(label="R_偏位",
                                     required=False,
                                     min_value=0,
                                     max_value=180,
                                     widget=widgets.TextInput(
                                         attrs={'id': 'r_deviation', 'placeholder': '偏位'}),
                                     error_messages={'min_value': '超出范围', 'max_value': '超出范围'},
                                     )
    r_add = forms.IntegerField(label="R_渐进",
                               required=False,
                               min_value=50,
                               max_value=400,
                               widget=widgets.TextInput(
                                   attrs={'id': 'r_add', 'placeholder': 'ADD'}),
                               error_messages={'min_value': '不能小于50', 'max_value': '不能超过500'},
                               )
    r_pd = forms.IntegerField(label="瞳距",
                              required=False,
                              min_value=43,
                              max_value=83,
                              widget=widgets.TextInput(
                                  attrs={'id': 'r_pd', 'placeholder': '瞳距'}),
                              error_messages={'min_value': '43', 'max_value': '83'},
                              )
    frame = forms.CharField(label="镜框",
                            required=False,
                            max_length=20,
                            widget=widgets.TextInput(
                                attrs={'id': 'frame', 'placeholder': '镜框'}),
                            validators=[RegexValidator(r'^[\u4E00-\u9FA5A-Za-z0-9_]+$', '不能输入特殊字符')],
                            error_messages={'max_value': '超出范围'},
                            )
    todo = forms.CharField(label="备注",
                           required=False,
                           strip=True,
                           max_length=2000,
                           widget=widgets.TextInput(
                               attrs={'id': 'todo', 'placeholder': '备注'}),
                           validators=[RegexValidator(r'^[\u4E00-\u9FA5A-Za-z0-9_]+$', '不能输入特殊字符')],
                           )