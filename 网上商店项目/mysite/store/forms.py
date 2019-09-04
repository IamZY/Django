from django import forms

class LoginForm(forms.Form):
    userid = forms.CharField(label="客户账号：",required=True)
    password = forms.CharField(label="客户密码：",widget=forms.PasswordInput)



class RegistrationForm(forms.Form):
    userid = forms.CharField(label='客户账号：', required=True)
    name = forms.CharField(label='客户姓名：', required=True)
    password1 = forms.CharField(label='客户密码：', widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次输入密码：', widget=forms.PasswordInput)
    birthday = forms.DateField(label='出生日期：', error_messages={'invalid': '输入的出生日期无效'})
    address = forms.CharField(label='通讯地址：', required=False)
    phone = forms.CharField(label='电话号码：', required=False)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('两次输入的密码不一致')

        return password2