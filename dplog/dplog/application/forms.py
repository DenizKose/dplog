from django import forms
from django.db.models import Q

from application.models import Application, ClientPerson, ClientAddress, Client, Store, Status
from users.models import Profile


class ApplicationForm(forms.ModelForm):
    order_1c = forms.CharField(label='Order 1C', max_length=127,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter order number'}))
    manager = forms.ModelChoiceField(label='Manager', queryset=Profile.objects.all().filter(status=2),
                                     widget=forms.Select(attrs={'class': 'form-select'}))
    notes = forms.CharField(label='Notes', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter notes here'}))
    client = forms.ModelChoiceField(label='Client', queryset=Client.objects.all(),
                                    widget=forms.TextInput(attrs={'class': 'form-select', 'list': 'clients_list'}))
    client_person = forms.ModelChoiceField(label='Client name', queryset=ClientPerson.objects.all(),
                                           widget=forms.TextInput(attrs={'class': 'form-select'}))
    client_address = forms.ModelChoiceField(label='Address', queryset=ClientAddress.objects.all(),
                                            widget=forms.TextInput(attrs={'class': 'form-select'}))
    store = forms.ModelChoiceField(label='Store', queryset=Store.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-select'}))
    order_date = forms.DateField(label='Order date', localize=False, widget=forms.DateInput(format='%Y-%m-%d',
                                                                                            attrs={
                                                                                                'class': 'form-control',
                                                                                                'type': 'date'}))
    order_time_start = forms.TimeField(label='From', required=False, localize=False,
                                       widget=forms.TimeInput(format='%H:%M',
                                                              attrs={
                                                                  'class': 'form-control',
                                                                  'type': 'time'}))
    order_time_end = forms.TimeField(label='To', required=False, localize=False, widget=forms.TimeInput(format='%H:%M',
                                                                                                        attrs={
                                                                                                            'class': 'form-control',
                                                                                                            'type': 'time'}))
    files = forms.FileField(label='File', required=False,
                            widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}))

    class Meta:
        model = Application
        exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')


class ChangeDriverForm(forms.ModelForm):
    driver = forms.ModelChoiceField(required=False, label='Driver', queryset=Profile.objects.all().filter(status=3),
                                    widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Application
        exclude = ('created_at', 'created_by', 'updated_at', 'updated_by',
                   'order_1c', 'manager', 'notes', 'client',
                   'client_person', 'client_address', 'store', 'order_date',
                   'order_time_start', 'order_time_end', 'order', 'files'
                   )


class AssignDriverPersonallyForm(forms.ModelForm):
    driver = forms.ModelChoiceField(required=False, label='Driver', queryset=Profile.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, user, *args, **kwargs):
        super(AssignDriverPersonallyForm, self).__init__(*args, **kwargs)
        self.fields['driver'].queryset = Profile.objects.filter(pk=user)


    class Meta:
        model = Application
        exclude = ('created_at', 'created_by', 'updated_at', 'updated_by',
                   'order_1c', 'manager', 'notes', 'client',
                   'client_person', 'client_address', 'store', 'order_date',
                   'order_time_start', 'order_time_end', 'order', 'files'
                   )


class ChangeStatusForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=False, label='Driver',
                                    queryset=Status.objects.all().filter(Q(pk=2) | Q(pk=3) | Q(pk=4) | Q(pk=5)),
                                    widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Application
        exclude = ('created_at', 'created_by', 'updated_at', 'updated_by',
                   'order_1c', 'manager', 'notes', 'driver', 'client',
                   'client_person', 'client_address', 'store', 'order_date',
                   'order_time_start', 'order_time_end', 'order', 'files'
                   )
