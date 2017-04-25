# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'home/grid.html')


def clueinput(request):
	clue = "No clue given"

	if request.method == "POST":
	#Get the posted form
		clue = request.POST['clue']
		clueno = request.POST['clueno']
		length = request.POST['length']
		direct = request.POST['type']
	return render(request, 'home/clue.html', {"clue" : direct,"clueno" : clueno,"length" : length,"type" : direct})