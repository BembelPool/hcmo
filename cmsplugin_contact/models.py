# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class Contact(CMSPlugin):
    SPAM_PROTECTION_CHOICES = (
        (0, 'Honeypot'),
        (1, 'Akismet'),
        (2, 'ReCAPTCHA'),
    )

    THEME_CHOICES = (
        ('clean', 'Clean'),
        ('red', 'Red'),
        ('white', 'White'),
        ('blackglass', 'Black Glass'),
        ('custom', 'Custom'),
    )

    site_email 	= models.EmailField(_('Email empfänger'))

    # labels
    givenname_label = models.CharField(_('Vorname'), default=_('Vorname'), max_length=100)
    surname_label   = models.CharField(_('Nachname'), default=_('Name'), max_length=100)
    email_label     = models.CharField(_('Email'), default=_('Email'), max_length=100)
    content_label   = models.CharField(_('Nachricht'), default=_('Message'), max_length=100)
    send_copy_label = models.CharField(_('Kopie an'), default=_('Kopie der Email an mich senden'), max_length=100)

    thanks  = models.CharField(verbose_name=_("Danke nachricht"), help_text=_('Nachricht wenn erfolgreich versendet wurde'), default=_('Vielen Dank.'), max_length=200)
    submit  = models.CharField(_('Abschicken'), default=_('Senden'), max_length=30)

    def __unicode__(self):
        return self.site_email
