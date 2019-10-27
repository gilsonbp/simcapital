from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CapitalUser(User):
    cpf = models.CharField(max_length=11, verbose_name=_('CPF'))
    birth_date = models.DateField(verbose_name=_('Birth date'))

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('Capital User')
        verbose_name_plural = _('Capital Users')
