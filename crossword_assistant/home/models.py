# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Clue(models.Model):
    clue = models.CharField(max_length=250)
    clue_number = models.PositiveIntegerField()
    answer_length = models.PositiveIntegerField()
    across_down = models.PositiveIntegerField()
