#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import *
from tkFileDialog import *

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

def moulinette():
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
	for word in line.split():
		if word.startswith("$$"):
			if word.endswith("$$"):
				variables.append(word)
				print word
f.close()

##GUI
mainWindow = Tk()
#Body
pMaster = PanedWindow(mainWindow, orient=HORIZONTAL)

#Labels
pLabels = PanedWindow(mainWindow, orient=VERTICAL)
pLabels.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
for variable in range(len(variables)):
	pLabels.add(Label(pLabels, text=variables[variable].replace("$$","")))
#Inputs
pInputs = PanedWindow(mainWindow, orient=VERTICAL)
for variable in range(len(variables)):
	result = StringVar()
	results.append(result)
	pInputs.add(Entry(mainWindow,textvariable=result))
#DEBUG


#Bouton
bouton=Button(mainWindow, text="Launch", command=moulinette)

#Main
pMaster.add(pLabels)
pMaster.add(pInputs)
pMaster.add(bouton)
pMaster.pack()

mainWindow.mainloop()

