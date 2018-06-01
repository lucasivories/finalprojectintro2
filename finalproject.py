#!/usr/bin/python
print "Content-type: text/html\n"

import cgi

#help you see errors
import cgitb
cgitb.enable()

head = '''<!DOCTYPE html>
<html>
  <head>
   <title>2017 NYC High School Directory</title>
  </head>
  <body>
'''

def convertToDictionary(fieldStorage):
   output = {}
   for key in fieldStorage.keys():
     output[key] = fieldStorage[key].value
   return output
   
form = convertToDictionary(cgi.FieldStorage()) 
   
fh = open("highschool.csv", "r")
data = fh.readlines() #returns a list, each item is a line
for row in data[1:]:
  #removes the \n character and turns each row from a string to an array of values
  row = row[:-1].split(",")
  
options = ""
fruits = ["apple", "orange", "banana", "durian"]
for fruit in fruits:
  options += "<option value={fruit}>{fruit}</option>".format(fruit = fruit)

dropdown = "<select>{options}</select>".format(options = options)
