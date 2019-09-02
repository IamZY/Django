from django import forms 

class RegistrationForm(forms.Form):
    username = forms.CharField(label = "用户名:",max_length=20)
    email = forms.EmailField(label = "邮箱:")
    password1 = forms.CharField(label = "密码:",widget = forms.PasswordInput())
    password2 = forms.CharField(label = "再次输入密码:", widget = forms.PasswordInput())
    birthday = forms.DateField(label = "出生日期:",error_messages = {"invalid":"输入的日期无效"})

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不匹配")
        return password2


class UploadFileForm(forms.Form):
    file = forms.FileField()