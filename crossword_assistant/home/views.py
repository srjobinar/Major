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
		v_n = request.POST['answer_type']
		query = Clue(clue = clue , clue_number = clueno , answer_length = length , across_down = direct, cell_number = cell_num,verb_noun=v_n)
		query.save()
	return HttpResponseRedirect("/")

def finish(request):
	data = Clue.objects.all()
	for d in data:
		if d.list_flag == 1:
			d.ans_list = json.loads(d.ans_list)
	return render(request,'home/solve_crossword.html',{'data':data})

def answer(request):
	if request.method == "POST":
		answer = request.POST['answer']
		clue_num = request.POST['clue_num']
		direct = request.POST['a_d']
		reg_exp = request.POST['reg_exp']
		dictionary = request.POST['dict']
		cl = ""+clue_num+direct
		print(cl)
		ndict = json.loads(dictionary)
		if direct == 'a':
			a_d = 1
			d = 0
			k=1
		else:
			d=1
			k=100
			a_d = 0
		clue = Clue.objects.all().filter(clue_number = clue_num,across_down = a_d)[0]
			# clue = Clue(clue_number = clue_num,across_down = a_d).objects
		clue.answer = answer
		if answer != "":
			clue.ans_flag = 1
		else:
			clue.ans_flag = 0	
		clue.save()
		arr = []
		for i in range(0,len(answer)):
			if reg_exp[i] != '_' and reg_exp[i]!=answer[i]:
				cell=clue.cell_number+(k*i)
				classes = str(ndict[str(cell)])
				classes = classes.replace(" ","")
				classes = classes.replace(cl,"")
				arr.append(classes)
		for i,val in enumerate(arr):
			if(d==1):
				val = val.replace("a","")
			else:
				val = val.replace("d","")
			clue = Clue.objects.all().filter(clue_number = val,across_down = d)[0]
			clue.answer = ""
			clue.ans_flag = 0
			clue.save()		
	return HttpResponseRedirect('/finish')

def solve(request):
	if request.method == "POST":
		clue_num = request.POST['solve_clue_num']
		direct = request.POST['solve_a_d']
		if direct == 'a':
			a_d = 1
		else:
			a_d = 0
		clue = Clue.objects.all().filter(clue_number = clue_num,across_down = a_d)[0]
		if clue.verb_noun == 1:
			a = find_ans.noun_fn(str(clue.clue),int(clue.answer_length))
		elif clue.verb_noun == 2:
			a = find_ans.verb_fn(str(clue.clue),int(clue.answer_length))
		else:
			a = find_ans.dont_know_fn(str(clue.clue),int(clue.answer_length))
		data = json.dumps(a)
		clue.ans_list = data
		clue.list_flag = 1
		clue.save()
	return HttpResponseRedirect('/finish')
