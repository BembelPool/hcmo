# -*- coding: utf-8 -*-
from django.forms import ModelForm, Field, CharField
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from models import Contact

"""
class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)
"""
