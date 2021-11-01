from django import forms
from django.contrib.auth.models import User, Group

from application.models import Store
from users.models import Profile, ProfileStatus


class StoreForm(forms.ModelForm):
    store_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    store_address = forms.CharField(max_length=2047, widget=forms.TextInput(attrs={'class': 'form-control'}))
    store_operators = forms.ModelMultipleChoiceField(queryset=Profile.objects.filter(status=4),
                                                     widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Store
        fields = ('store_name', 'store_address', 'store_operators')


class AdminUserForm(forms.ModelForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=31, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class AdminProfileForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=ProfileStatus.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(format='%Y-%m-%d', attrs={
        'class': 'form-control',
        'type': 'date'}))
    father_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('status', 'birth_date', 'father_name')
