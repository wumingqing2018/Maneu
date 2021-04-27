from django import forms


class GlassStoreInsert(forms.Form):
    brand = forms.CharField(
        label="品牌",
        strip=True,
        min_length=1,
        max_length=100,
        error_messages={'required': '请输入内容',
                        'min_length': '最少输入一个字',
                        'max_length': '最多输入一百个字'}
    )
    model = forms.CharField(
        label="型号",
        required=True,
        strip=True,
        min_length=1,
        max_length=100,
        error_messages={'required': '请输入内容',
                        'min_length': '最少输入一个字',
                        'max_length': '最多输入一百个字'}
    )
    sphere = forms.CharField(
        label="折射",
        required=True,
        strip=True,
        min_length=1,
        max_length=100,
        error_messages={'required': '请输入内容',
                        'min_length': '最少输入一个字',
                        'max_length': '最多输入一百个字'}
    )
    astigmatic = forms.CharField(
        label="折射",
        required=True,
        strip=True,
        min_length=1,
        max_length=100,
        error_messages={'required': '请输入内容',
                        'min_length': '最少输入一个字',
                        'max_length': '最多输入一百个字'}
    )
    refraction = forms.CharField(
        label="折射",
        required=True,
        strip=True,
        min_length=1,
        max_length=100,
        error_messages={'required': '请输入内容',
                        'min_length': '最少输入一个字',
                        'max_length': '最多输入一百个字'}
    )
    remark = forms.CharField(
        label="备注",
        required=True,
        strip=True,
        min_length=1,
        max_length=100,
        error_messages={'required': '请输入内容',
                        'min_length': '最少输入一个字',
                        'max_length': '最多输入一百个字'}
    )
