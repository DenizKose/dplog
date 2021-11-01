from django.db import models
from users.models import Profile


class Application(models.Model):
    order = models.IntegerField(default=None, editable=False, unique=True, verbose_name='ID number')
    order_1c = models.CharField(max_length=127, blank=True, verbose_name='1C order')
    driver = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Driver', null=True, blank=True,
                               related_name='driver')
    manager = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Manager', blank=True,
                                related_name='manager')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True)
    status = models.ForeignKey('Status', default=2, on_delete=models.CASCADE, blank=True, verbose_name='Status')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, blank=True, verbose_name='Client')
    client_person = models.ForeignKey('ClientPerson', blank=True, on_delete=models.CASCADE,
                                      verbose_name='Contact name')
    client_address = models.ForeignKey('ClientAddress', blank=True, on_delete=models.CASCADE,
                                       verbose_name='Contact address')
    store = models.ForeignKey('Store', verbose_name='Store', on_delete=models.CASCADE, blank=True)
    order_date = models.DateField(null=True, blank=True, verbose_name='Order date')
    order_time_start = models.TimeField(null=True, blank=True, verbose_name='Delivery start')
    order_time_end = models.TimeField(null=True, blank=True, verbose_name='Delivery end')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created at')
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, verbose_name='Created by',
                                   related_name='created_by')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    updated_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Updated by',
                                   related_name='updated_by')
    files = models.FileField(upload_to='order_files/', verbose_name='Files', null=True, blank=True)

    def __str__(self):
        return str(self.order)


class Status(models.Model):
    status_name = models.CharField(max_length=127, verbose_name='Status')

    def __str__(self):
        return str(self.status_name)


class Store(models.Model):
    store_name = models.CharField(max_length=127, verbose_name='Store')
    store_address = models.CharField(max_length=255, verbose_name='Store address', blank=True, null=True)
    store_operators = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return str(self.store_name)


class Client(models.Model):
    client_name = models.CharField(max_length=127, verbose_name='Client name')
    client_itn = models.IntegerField(help_text='Individual Taxpayer Number', verbose_name='ITN', null=True, blank=True)
    client_1c_id = models.CharField(max_length=127, help_text='ID in 1C', verbose_name='1C ID', null=True, blank=True)

    def __str__(self):
        return str(self.client_name)


class ClientPerson(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
    client_person_name = models.CharField(max_length=127, verbose_name='Contact name')
    client_person_tel = models.CharField(max_length=127, verbose_name='Contact tel', null=True, blank=True)
    client_person_email = models.CharField(max_length=127, verbose_name='Contact email', null=True, blank=True)
    client_person_notes = models.TextField(verbose_name='Contact notes', null=True, blank=True)

    def __str__(self):
        return str(self.client_person_name)


class ClientAddress(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
    address = models.CharField(max_length=127, verbose_name='Address')
    address_notes = models.CharField(max_length=4095, verbose_name='Notes', null=True, blank=True)

    def __str__(self):
        return str(self.address)
