from django.db import models
from django.utils.translation import gettext_lazy as _
from pyexpat.errors import messages


class ContactModel(models.Model):
    full_name = models.CharField(max_length=128 , verbose_name=_("ful name") )
    email = models.EmailField(verbose_name=_("email"))
    subject = models.CharField(max_length=255 ,verbose_name=_('subject'))
    message= models.TextField(verbose_name=_('messages'))


    def __str__(self):
        return f"{self.full_name},{self.subject}"


    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

