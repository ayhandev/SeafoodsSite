from django import forms
from .models import FormsRegister, Product, EmailRegister, Review


class FormsRegisterForm(forms.ModelForm):
    class Meta:
        model = FormsRegister
        fields = ['full_name', 'phone', 'email', 'message']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'region', 'user']



class EmailRegisterForm(forms.ModelForm):
    class Meta:
        model = EmailRegister
        fields = ['email']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'description']

#  сделал Айхан
