# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Test_A(models.Model):

    #__Test_A_FIELDS__
    test_fn_1 = models.TextField(max_length=255, null=True, blank=True)
    test_fn_2 = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Test_A_FIELDS__END

    class Meta:
        verbose_name        = _("Test_A")
        verbose_name_plural = _("Test_A")



#__MODELS__END
