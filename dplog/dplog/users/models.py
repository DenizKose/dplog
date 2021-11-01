from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey('ProfileStatus', on_delete=models.CASCADE, verbose_name='Status', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        name = []
        if self.user.first_name is not None:
            name.append(self.user.first_name)
        if self.user.last_name:
            name.append(self.user.last_name)
        if self.father_name:
            name.append(self.father_name)
        return ' '.join(name)


class ProfileStatus(models.Model):
    profile_status_name = models.CharField(verbose_name='Status', max_length=127)

    def __str__(self):
        return str(self.profile_status_name)