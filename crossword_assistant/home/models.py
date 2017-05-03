# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Clue(models.Model):
    clue = models.CharField(max_length=250)
    clue_number = models.PositiveIntegerField()
    answer_length = models.PositiveIntegerField()
    across_down = models.PositiveIntegerField()
    cell_number = models.PositiveIntegerField()
    answer = models.CharField(max_length=1000, default="")
    ans_flag = models.PositiveIntegerField(default=0)
    verb_noun = models.PositiveIntegerField(default=1)
    ans_list = models.CharField(max_length=62000, default="")
    list_flag = models.PositiveIntegerField(default=0)
    compound_flag = models.PositiveIntegerField(default=0)
