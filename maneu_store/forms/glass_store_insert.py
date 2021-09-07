from django import forms


class GlassStoreInsert(forms.Form):
    brand = forms.CharField(label="品牌",
                            strip=True,
                            min_length=1,
                            max_length=100,
                            error_messages={'required': '请输入内容',
                                            'min_length': '最少输入1位字符',
                                            'max_length': '最多输入100位字符'}
                            )
    model = forms.CharField(label="型号",
                            required=True,
                            strip=True,
                            min_length=1,
                            max_length=100,
                            error_messages={'required': '请输入内容',
                                            'min_length': '最少输入1位字符',
                                            'max_length': '最多输入100位字符'}
                            )
    count = forms.CharField(required=True,
                            strip=True,
                            min_length=1,
                            max_length=100,
                            error_messages={'required': '请输入内容',
                                            'min_length': '最少输入1位字符',
                                            'max_length': '最多输入100位字符'}
                            )
    sphere = forms.CharField(label="折射",
                             required=True,
                             strip=True,
                             min_length=1,
                             max_length=100,
                             error_messages={'required': '请输入内容',
                                             'min_length': '最少输入1位字符',
                                             'max_length': '最多输入100位字符'}
                             )
    astigmatic = forms.CharField(label="折射",
                                 required=True,
                                 strip=True,
                                 min_length=1,
                                 max_length=100,
                                 error_messages={'required': '请输入内容',
                                                 'min_length': '最少输入1位字符',
                                                 'max_length': '最多输入100位字符'}
                                 )
    refraction = forms.CharField(label="折射",
                                 required=True,
                                 strip=True,
                                 min_length=1,
                                 max_length=100,
                                 error_messages={'required': '请输入内容',
                                                 'min_length': '最少输入1位字符',
                                                 'max_length': '最多输入100位字符'}
                                 )
    remark = forms.CharField(label="备注",
                             required=False,
                             strip=True,
                             max_length=255,
                             error_messages={'max_length': '最多输入255个字'}
                             )
