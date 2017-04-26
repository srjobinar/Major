# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Clue
def index(request):
	data = Clue.objects.all()
	return render(request,'home/grid.html',{'data':data})


def clueinput(request):
	if request.method == "POST":
	#Get the posted form
		clue = request.POST['clue']
		clueno = request.POST['clueno']
		length = request.POST['length']
		direct = request.POST['type']
		cell_num = request.POST['cell_num']
		query = Clue(clue = clue , clue_number = clueno , answer_length = length , across_down = direct, cell_number = cell_num)
		query.save()
	return HttpResponseRedirect("/")

def finish(request):
	data = Clue.objects.all()
	return render(request,'home/solve_crossword.html',{'data':data})
