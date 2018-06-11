#!/usr/bin/python
print "Content-type: text/html\n"

import cgi

# displays error messages in your browser
import cgitb
cgitb.enable()

# function that will package all form information in a python dictionary
def convertToDictionary(fieldStorage):
   output = {}
   for key in fieldStorage.keys():
     output[key] = fieldStorage[key].value
   return output

def readFile():
    import csv
    with open("highschool.csv") as file:
    	reader = csv.DictReader(file)
    	data = [r for r in reader]
    	return data

readFile()

data = readFile()

def findSchool(data):
   info  = []
   for row in data:
         info.append(row['school_name'])
         info.append(row['boro'])
         info.append(row['advancedplacement_courses'])
         info.append(row['website'])
         info.append(row['total_students'])
   return info

def main():
   form = convertToDictionary(cgi.FieldStorage())
   print form
   print "<br>"

   header = ['School', 'Borough', 'Website', 'Total students', 'School', 'Borough', 'Website', 'Total students',
   'School', 'Borough', 'Website', 'Total students', 'School', 'Borough', 'Website', 'Total students', 'School', 'Borough', 'Website', 'Total students']
      info_2 = findSchool(data)
      for i in range(len(info_2)):
          if header[i] == 'Total students':
             print header[i], ':', info[i], '<p>'
          else:
             print header[i], ':', info[i], '<br>'

print '''<!DOCTYPE html>
<html>
  <head>
   <title>Your Results!</title>
  </head>
  <body>'''

print ''' </body>
</html>'''

main()
