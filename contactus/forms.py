from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'نام و نام خانوادگی شما', 'data-error': 'نام و نام خانوادگی را وارد کنید'}),
            'meli_code': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'کد ملی شما', 'data-error': 'کد ملی را وارد کنید'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'ایمیل شما', 'data-error': 'ایمیل خود را وارد کنید'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'تلفن شما', 'data-error': 'شماره تلفن خود را وارد کنید'}),
            'message': forms.Textarea(attrs={'class': 'form-control costume_message', 'required': 'true', 'cols': '30', 'rows': '5', 'placeholder': 'توضیحات شما', 'data-error': 'توضیحات مد نظر را وارد کنید'}),
        }