from django import forms 
import re
from django.contrib.auth.models import User 
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form): 
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password_1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput)
    
    def clean_password_2(self):
        if 'password_1' in self.cleaned_data:
            password_1 = self.cleaned_data['password_1']
            password_2 = self.cleaned_data['password_2']
            if password_1!= password_2:
                raise forms.ValidationError('Mật khẩu không khớp')
        return password_2
    
    def clean_username(self): 
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tên tài khoản có kí tự đặc biệt')
        try: 
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tên tài khoản đã tồn tại')
    
    def save(self): 
        User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password_1'])
        