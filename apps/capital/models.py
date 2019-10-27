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


class Salary(models.Model):
    capital_user = models.ForeignKey(
        CapitalUser,
        verbose_name=_('Capital User'),
        on_delete=models.CASCADE,
        related_name='salary'
    )
    salary_date = models.DateField(
        verbose_name=_('Salary Date')
    )
    salary_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('Salary Value')
    )
    salary_discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('Salary Discount')
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('capital_user', 'salary_date')
        verbose_name = _('Salary')
        verbose_name_plural = _('Salaries')
