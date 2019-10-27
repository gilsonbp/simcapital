import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin, Permission, Group
)
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class SIMPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = _('Permission')
        verbose_name_plural = _('Permissions')


class SIMGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError(_('Users must have an email.'))

        user = self.model(
            email=email,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        if not password:
            password = 123456
        user = self.create_user(
            email=email,
            name=name,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name=_('Email'), unique=True,
                              help_text=_(
                                  "The email will be used to access the "
                                  "system and send information"),
                              validators=[validators.EmailValidator()],
                              error_messages={
                                  'unique': _('This email already exists.'),
                              })
    name = models.CharField(max_length=200, verbose_name=_('Name'),
                            help_text=_("Enter the user's full name."))
    is_active = models.BooleanField(default=True, verbose_name=_('Active?'),
                                    help_text=_(
                                        'Only active users can '
                                        'access the system.'))
    is_staff = models.BooleanField(default=False,
                                   verbose_name=_('Is part of the team?'),
                                   help_text=_(
                                       'Determines whether the user has '
                                       'access to the system panel.'))
    date_joined = models.DateTimeField(
        _('Registration date'), default=timezone.now
    )

    email_confirmation = models.CharField(
        max_length=250, verbose_name=_('E-mail Confirmation'), null=True)

    groups = models.ManyToManyField(
        SIMGroup,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        SIMPermission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ('email',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.name

    get_full_name.short_description = _('Full name')
