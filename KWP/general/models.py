from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models

from lookup_tables.models import *


class TrapLocation(models.Model):
	loc = models.PointField(null=True,blank=True)
	trap_type = models.ForeignKey(TrapType)
	trap_number = models.PositiveIntegerField()
	site = models.ForeignKey(Site)
	notes = models.TextField(null=True,blank=True)

class TrapCheck(models.Model):
	loc = models.PointField(null=True, blank=True)
	trap_loc = models.ForeignKey(TrapLocation)
	site = models.ForeignKey(Site)
	sublocation = models.ForeignKey(Infrastructure)
	trap_date = models.DateField(default=timezone.now)
	arrival_status = models.CharField(max_length=50)
	arrival_bait = models.ForeignKey(Bait)
	
