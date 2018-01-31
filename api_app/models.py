# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


from api_app.manager import CustomUserManager


# class SocialUser(AbstractBaseUser):
#     """
#     this class is a model for Users of the application
#     """
#
#     username = models.CharField(max_length=50, unique=True)
#     # password = models.CharField(max_length=50)
#     # email = models.CharField(max_length=50, unique=True)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['username']
#     objects = CustomUserManager()
#
#     class Meta:
#         managed = True
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         """:returns return full name of user"""
#         full_name = '%s %s' %(self.firstName, self.lastName)
#         return full_name.strip()
#
#     def get_short_name(self):
#         """:returns return first name of the user"""
#         return self.firstName
#
#     def is_staff(self):
#         return self.is_admin
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return self.is_admin
#
#     def __str__(self):
#         return self.username


class Information(models.Model):
    string_diary = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.string_diary

