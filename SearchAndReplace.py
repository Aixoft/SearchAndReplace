#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import *
from tkFileDialog import *

import re
import os, sys

if len(sys.argv) <> 3:
	if len(sys.argv) == 1:
		fileInName = askopenfilename(title="InputFile",filetypes=[('text files','.txt'),('all files','.*')])
		fileOutName = asksaveasfile(title="OutputFile",mode='w')

	else:
		print "Syntax: "+sys.argv[0]+" [input file] [output file]"
		sys.exit()
else:
	fileInName = sys.argv[1]
	fileOutName = sys.argv[2]

def findBetween(s):
	return re.findall ('\$\$(.*?)\$\$', s, re.MULTILINE)

def convertFile():
	fileOut = open(fileOutName,"a")
	with open(fileInName,"r") as fileIn:
    		data=fileIn.read()

	for index, item in enumerate(variables):
		data=data.replace(variables[index],results[index].get())

	fileOut.write(data)
	fileIn.close()
	fileOut.close()
	mainWindow.quit()

#Read file
variables = []
results = []
print "Opening and reading: "+fileInName
f =  open(fileInName,"r")
for line in f:
	words = findBetween(line)
	if len(words) == 1:
		word = words[0]
		variables.append(word)
		print word
	elif len(words) > 1:
		for word in words:
			variables.append(word)
			print word

f.close()

#GUI
mainWindow = Tk()

#Body
mainWindow.rowconfigure(len(variables), weight=1)
mainWindow.columnconfigure(3, weight=1)

#Labels
i=0
for variable in range(len(variables)):
	myLabel = Label(mainWindow, width=20, anchor=CENTER, text=variables[variable].replace("$$",""))
	myLabel.grid(row=i, column=0, sticky="nsew")
	i+=1
#Inputs
i=0
for variable in range(len(variables)):
	result = StringVar()
	results.append(result)
	myEntry = Entry(mainWindow, width=20, textvariable=result)
	myEntry.grid(row=i, column=1, sticky="nsew")
	i+=1

#DEBUG


#Bouton
bouton=Button(mainWindow, text="Launch", command=convertFile)
bouton.grid(row=0, column=2, rowspan=len(variables) ,sticky="nsew")

#Main
mainWindow.mainloop()

