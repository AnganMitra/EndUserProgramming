#!/usr/bin/env python
__author__ = "Angan Mitra"

import nltk as nlp
def readText(filename):
	delimiter='#'

	corpus = open(filename).read().split(delimiter)
	if len(corpus)!=4:
		print "Incomplete Description Submitted"
	domain = corpus[1].strip("Domain:").strip()
	env = corpus[2].strip("Environment:").strip()
	action  = corpus[3].strip("Action:").strip()

	return (domain, env, action)

class Predicate(object):
	"""docstring for Predicate"""
	def __init__(self):
		super(Predicate, self).__init__()
		self.predicate_name =""
		self.object_dealt=[]

	def add_name(self,name):
		self.predicate_name = name

	def add_block(self,block):
		self.object_dealt.append(block)

	def empty_predicate(self):
		if self.predicate_name == "" : # there can exist true predicates
			return True
		else:
			return False


	def generate_predicate_string(self):
		if self.empty_predicate():
			return ""
		pred_string = "( " + self.predicate_name
		var = 'a'
		index = 0
		for block in self.object_dealt:
			pred_string +=  " ?" + chr(ord(var) + index ) +  " - " + block + " " 
			index +=1
		pred_string += ")"
		return pred_string

# class Rule(object):
# 	"""docstring for Rule"""
# 	def __init__(self, rule):
# 		super(Rule, self).__init__()
# 		self.corpora = rule.split('.')

# 	def generate_predicate_string(self):
# 		predicate_string =""
# 		return predicate_string

class Environment(object):
	"""docstring for Environment"""
	def __init__(self, env):
		super(Environment, self).__init__()
		self.corpora = env.split('.')
		self.types=[]
		self.predicate_list=[]

	def parse_type(self):
		for line in self.corpora:
			if 'element' not in line:
				continue
			text = nlp.word_tokenize(line)
			tokens = nlp.pos_tag(text, tagset = 'universal')
			for token in tokens:
				if token[1]=='NOUN' and 'element' not in token[0]:
					self.types.append(token[0].lower())

	def generate_type_string(self):
		type_string = "(:types "
		for type_kind in self.types:
			type_string += type_kind + " "
		type_string += ")"
		return type_string

	def parse_predicates(self):
		for line in self.corpora:
			if 'element' in line:
				continue
			pred = Predicate()
			text = nlp.word_tokenize(line)
			tokens = nlp.pos_tag(text, tagset = 'universal')
			for token in tokens:
				if 'VERB' in token[1]:
					pred.add_name(token[0])
				if 'NOUN'  in token[1] and token[0].lower() in self.types:
					pred.add_block(token[0].lower())
			if not pred.empty_predicate():
				self.predicate_list.append(pred)

	def generate_predicate_string(self):
		predicate_string = "\n( predicates: \n"
		for pred in self.predicate_list:
			predicate_string += pred.generate_predicate_string() + "\n"
		predicate_string += ")"+"\n"
		return predicate_string

	def get_predicates(self):
		return self.predicate_list

	def get_types(self):
		return self.types
		
class ActionType(object):
	"""docstring for  ActionType"""
	def __init__(self, types, predicates):
		super( ActionType, self).__init__()
		self.types = types
		self.predicates = predicates
		self.action_name = ""
		self.parameters = []
		self.precondition = []
		self.effect = []


	def process_parameter_string(self, corpora):
		parameter_string = ":parameters ( "
		parameters = []
		for line in corpora:
			text = nlp.word_tokenize(line)
			tokens = nlp.pos_tag(text, tagset = 'universal')
			for token in tokens:
				if 'NOUN'  in token[1] and token[0].lower() in self.types:
					parameters.append(token[0].lower())
		var = 'a'
		index = 0
		for block in parameters:
			parameter_string +=  " ?" + chr(ord(var) + index) +  " - " + block + " " 
			index +=1
		parameter_string += " )"
		self.parameters.append(parameter_string)
		return 

	def process_precondition_string(self, corpora):
		precondition_string = ":precondition ( "
		# for line in corpora:
		# 	text = nlp.word_tokenize(line)
		# 	tokens = nlp.pos_tag(text, tagset = 'universal')
		# 	for token in tokens:
		# 		if 'NOUN'  in token[1] and token[0].lower() in self.types:
		# 			self.parameters.append(token[0].lower())
		# var = 'a'
		# index = 0
		# for block in self.parameters:
		# 	parameter_string +=  " ?" + chr(ord(var) + index) +  " - " + block + " " 
		# 	index +=1

		precondition_string += " )"
		self.precondition.append(precondition_string)
		return 

	def process_effect_string(self, corpora):
		effect_string = ":effect ( "
		# for line in corpora:
		# 	text = nlp.word_tokenize(line)
		# 	tokens = nlp.pos_tag(text, tagset = 'universal')
		# 	for token in tokens:
		# 		if 'NOUN'  in token[1] and token[0].lower() in self.types:
		# 			self.parameters.append(token[0].lower())
		# var = 'a'
		# index = 0
		# for block in self.parameters:
		# 	parameter_string +=  " ?" + chr(ord(var) + index) +  " - " + block + " " 
		# 	index +=1

		effect_string += " )"
		self.effect.append(effect_string)
		return 
						

	def process_logic(self, name, precondition, effect):
		if len(name) == 0:
			print "No action name definition in "
			return
		text = nlp.word_tokenize(name)
		tokens = nlp.pos_tag(text, tagset = 'universal')
		for token in tokens:
				if 'VERB'  in token[1]:
					self.action_name = token[0].lower()
		self.process_parameter_string( precondition + effect)
		self.process_precondition_string(precondition)
		self.process_effect_string(effect)
		return

	def generate_name_string(self):
		return self.action_name;

	def generate_parameter_string( self):
		return self.parameters[0]

	def generate_precondition_string(self):
		# print self.precondition[0]
		return self.precondition[0]

	def generate_effect_string(self):
		return self.effect[0]


class Action(object):
	"""docstring for Goal"""
	def __init__(self, action):
		super(Action, self).__init__()
		self.corpora = action.split('.')
		self.action_list=[]


	def process_actions(self,env_obj):
		types = env_obj.get_types()
		predicates = env_obj.get_predicates()
		act = ActionType(types, predicates)
		precondition =  []
		effect = []
		name = ""
		for line in self.corpora:
			if 'define' in line:
				name=line				
			if 'precondition' in line:
				precondition.append(line)
			if 'effect' in line:
				effect.append(line)
		act.process_logic(name, precondition, effect)
		self.action_list.append(act)
		return

	def generate_action_string(self):
		action_string = ""
		for action in self.action_list:
			action_string ="\n( action " + action.generate_name_string()
			action_string += "\n " + action.generate_parameter_string()
			action_string += "\n " + action.generate_precondition_string()
			action_string += "\n " + action.generate_effect_string()
			action_string += "\n)\n"
		return action_string


class Domain(object):
	"""docstring for Domain"""
	def __init__(self, domain):
		super(Domain, self).__init__()
		self.domain_name = domain

		
	def generate_domain_string(self):
		return "(define (domain " + str(self.domain_name) + ")"

	def generate_domain_requirements(self):
		return "(:requirements :strips :typing)"


def main():
	filename = "C:\Users\Prime\OneDrive\TER\src\data\description.txt"
	(domain,env, action )= readText(filename)
	domain_obj = Domain(domain)
	env_obj = Environment(env)
	action_obj = Action(action)
	
	print domain_obj.generate_domain_string()
	print domain_obj.generate_domain_requirements()

	env_obj.parse_type()
	env_obj.parse_predicates()

	print env_obj.generate_type_string()
	print env_obj.generate_predicate_string()

	action_obj.process_actions(env_obj)
	
	print action_obj.generate_action_string()
	print ")"  # to close the starting domain

if __name__ == '__main__':
	main()
