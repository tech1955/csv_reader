import json
import sys
import os

def csv2dict(path,file_name):
	# Read from txt file
	try:
		new_path = path+file_name
		f = open(new_path,"r")
		d2=f.read()
	except:
		print("\n\n\file not found....!\n\n\n")
	
	d2=d2.encode().decode('utf-8-sig') 
		
	l=d2.split("\n")
	row_list = l[1:]
	col_list = l[0].split(",")
	f.close()
	# refresh the data
	col_list = strip_list(col_list)
	d = covert2dict(col_list,row_list)
	return d
	
def strip_list(mylist):
	l=[]
	for i in mylist:
		if i.isalnum():
			l.append(i.strip())
		else :
			l.append(i)
		
	return l

def covert2dict(colms,rows):
	
	l = len(rows)
	dl = {}
	for i in range(len(rows)-1):
		k = 0
		for j in rows[i].split(","):
			if rows[0]==rows[i]:
				dl[colms[k]] = []
				dl[colms[k]] = [j.strip()]
			else:
				nl = dl[colms[k]]
				nl.append(j.strip())
				dl[colms[k]] = nl
			k = k + 1
		
	return dl	

def checkSpaces(mylist):
	sp =0
	for i in mylist:
		if sp < len(i):
			sp = len(i)
	return sp


def print2csv(d):
	colm = list(d.keys())
	rows = list(d.values())
	
	
	nl = rows
	for i in range(len(colm)):
		nl[i].append(colm[i])
	
	sp_list = []
	for i in nl:
		sp_list.append(checkSpaces(i))


	print("\n\n")
	for i in range(len(colm)):
		o="{:^"+str(sp_list[i]+2)+"}"
		print(o.format(colm[i]),end="")
	print("\n\n")
	
	for i in range(len(rows[0])-1):
		
		for j in range(len(colm)):
			v = d[colm[j]][i]
			o="{:^"+str(sp_list[j]+2)+"}"
			print(o.format(v),end="")
		print()


path = str(os.getcwd()) + "/"

file_name = "TechCrunchcontinentalUSA.csv"

d = csv2dict(path,file_name)

#print(d)
print2csv(d)

