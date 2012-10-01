#coding:utf-8

def split_string(source,split_string):
	output = []
	atsplit = True
	for char in source:
		if char in splitlist:
			atsplit = True

		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				output[-1] = output[-1] + char