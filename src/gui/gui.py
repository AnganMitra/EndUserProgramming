from tkinter import *



def generate_type_string(types):
	if len(types) == 0:
		print ("(:requirements :strips )")
		return 
	types = types.split(',')
	type_string = "(:types "
	for type_kind in types:
		type_string += type_kind.strip() + " "
	type_string += ")"
	print (type_string)
	print ("(:requirements :strips :typing)")
	return types

def generate_domain_string(domain_name):
	if len(domain_name)== 0:
		return False
	print ("(define (domain " + str(domain_name) + ")")
	return True

def generate_document(domain_name, types):
	if not generate_domain_string(domain_name):
		print ("error")
		return
	types = generate_type_string(types)
	print (")")  # closing brace of the starting domain
	return types

action_name=[]
checkbox_predicates= []
def add_action():
	global action_name
	global rowcount
	rowcount += 1	
	Label(master, text="Action name").grid(row = rowcount,column = 0)
	action_name.append(Entry(master))
	action_name[-1].grid(row = rowcount,column = 1)
	rowcount+=1
	Label(master, text="Description").grid(row = rowcount,column = 0)
	for entry in predicate_name:
		checkbox_predicates.append(IntVar())
		Checkbutton(master, text=entry, variable=checkbox_predicates[-1]).grid(row=rowcount)
		rowcount += 1
	Button(master, text='Add More Actions', command=add_action).grid(row=rowcount, column = 1)
	rowcount += 1
	return

def generate_predicate():
	print ("(:predicates ")
	global predicate_name
	for index  in range(len(predicate_name)):
		if predicate_name[index].get().strip() == "":
			continue		
		corpora =  predicate[index].get().strip().split()
		if len(corpora) == 0:
			continue
		_types = []
		for token in corpora:
			if token.lower() in types:
				_types.append(token.lower())
		pred_string = "(" + predicate_name[index].get().strip().lower()
		var = 'a'
		index = 0
		for token in _types:
			pred_string +=  " ?" + chr(ord(var) + index ) +  " - " + token + " " 
			index +=1
		pred_string += ")"
		print (pred_string)
	print (")")
	add_action()
	return

def add_predicate():
	global rowcount
	global types
	global predicate_name
	Label(master, text="States of objects").grid(row = rowcount,column = 0) 
	rowcount += 1	
	Label(master, text="State name").grid(row = rowcount,column = 0)
	predicate_name.append(Entry(master))
	predicate_name[-1].grid(row = rowcount,column = 1)
	rowcount+=1
	Label(master, text="Description").grid(row = rowcount,column = 0)
	predicate.append(Entry(master))
	predicate[-1].grid(row = rowcount,column = 1)
	rowcount+=1
	return

def add_action():
	generate_predicate()
	return

def generate_name_type():
	global rowcount
	global types
	domain_name = e1.get()
	types = e2.get().strip()
	types = generate_document(domain_name, types)
	
	Button(master, text='Add Predicates', command=add_predicate).grid(row=rowcount, column = 0)
	Button(master, text='Add Actions', command=generate_predicate).grid(row=rowcount, column = 1)
	

	rowcount+=1
	return

types = None
predicate_name = []
predicate = []
rowcount = 4

master = Tk()
master.title("Input Specification")
Label(master, text="Domain Name").grid(row=0)
Label(master, text="Objects involved").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)



e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


# Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Next', command=generate_name_type).grid(row=3, column=0, sticky=W, pady=4)

# top = Toplevel()
# t1 = Text(top)
# top.title("Generated Text")

mainloop( )
