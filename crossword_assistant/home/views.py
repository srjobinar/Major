# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Clue
from . import find_ans
import json

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
	for d in data:
		if d.ans_flag == 0:
			d.answer = json.loads(d.answer)
	return render(request,'home/solve_crossword.html',{'data':data})

def answer(request):
	if request.method == "POST":
		answer = request.POST['answer']
		clue_num = request.POST['clue_num']
		direct = request.POST['a_d']
		v_n = request.POST['type']
		if direct == 'a':
			a_d = 1
		else:
			a_d = 0	
		clue = Clue.objects.all().filter(clue_number = clue_num,across_down = a_d)[0]	
		if answer != "":
			# clue = Clue(clue_number = clue_num,across_down = a_d).objects
			clue.answer = answer
			clue.ans_flag = 1
			clue.save()
		else:
			a = find_ans.algorithm(str(clue.clue),int(clue.answer_length))
			data = json.dumps(a)
			clue.answer = data
			clue.verb_noun = v_n
			clue.save()
	return HttpResponseRedirect('/finish')