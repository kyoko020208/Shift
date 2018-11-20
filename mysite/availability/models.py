from django.contrib.auth.models import AbstructUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

class Restaurants(models.Model):
    """
    Create Restaurants Table
    """
    class Meta:
        db_table = 'restaurants'

    name = models.CharField(_('Restaurants'), max_length=150)

    def __str__(self):
        return self.name



class Employee(AbstructUser, PermissionsMixin):
    """
    Create Employee Table
    """

    class Meta:
        db_table = 'Employee'

    username_validator = UnicodeUsernameValidator

    #Create an employee with given first_name, last_name, phone and password
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    phone = models.CharField(_('Phone Number'), max_length=15)
    password = models.CharField(_('password'), max_length=128)


    #Check if he already exists in the list
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )


    #Check if he is a manager
    is_manager = models.BooleanField(
        _('manager status'),
        default=False,
    )

    # Check if the account is active
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

