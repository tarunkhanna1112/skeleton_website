from flask import render_template, request, redirect, flash, session, Response
from app import app
from app.forms import SearchForm, SearchForm1

import os, json, random

import numpy as np

common_title = "skeleton_website"

@app.route('/',methods=['GET', 'POST'])
@app.route('/home',methods=['GET', 'POST'])
def home():
	try:
		del(session['message1'])
		del(session['message2'])
	except:
		pass

	form = SearchForm(prefix="form1")
	if form.submit1.data:
		if form.data['search1'] != "":
			session['message1'] = form.data['search1']
			return(redirect('/search'))

	return render_template('home.html',title=common_title,form=form)

@app.route('/search',methods=['GET', 'POST'])
def search_results():
	temp1, temp2 = random.randint(0,16777215), random.randint(0,16777215)
	default_output = "{}{}".format(hex(temp1),hex(temp2))
	#default_output = "tmp"

	output_dir = "tmp_dir/{}".format(default_output)
	if os.path.exists(output_dir) == False:
		os.mkdir(output_dir)
		
	form1 = SearchForm1(prefix="form1")
	if form1.submit2.data or form1.submit3.data:
		inputquery = session.get('message1')
		
		with open("{}/response1.json".format(output_dir),"r") as file:
			json_obj = json.load(file)

			data = json_obj["filters"]
			meta_data = json_obj["meta"]["filters"]
	else:
		inputquery = session.get('message1')

		#os.system("curl")

		with open("{}/response.json".format(output_dir),"r") as file:
			json_obj = json.load(file)

			data = json_obj["filters"]
			meta_data = json_obj["meta"]["filters"]

	return render_template('page1.html',title=common_title,data=data,meta_data=meta_data, form=form1)
	