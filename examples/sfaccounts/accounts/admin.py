# django-salesforce
#
# by Phil Christensen
# (c) 2012 Working Today
# See LICENSE.md for details
#

from django.contrib import admin
from django.db import models
from django.forms import widgets
from django.http import HttpResponse

from salesforce import models
from salesforce.admin import RoutedModelAdmin

class AccountAdmin(RoutedModelAdmin):
	list_display = ('Name', 'Salutation', 'FirstName', 'LastName', 'PersonEmail')
admin.site.register(models.Account, AccountAdmin)

class LeadAdmin(RoutedModelAdmin):
	list_display = ('Salutation', 'FirstName', 'LastName', 'Email')
admin.site.register(models.Lead, LeadAdmin)

class ChargentOrderAdmin(RoutedModelAdmin):
	list_display = ('Status', 'Total', 'Balance_Due', 'CreatedDate', 'CreatedById')
admin.site.register(models.ChargentOrder, ChargentOrderAdmin)