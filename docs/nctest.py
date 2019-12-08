#!/usr/bin/python 
import random
print "Content-type: text/html\n" 

f= open("myfile.txt","r")
x=f.readlines()
random.shuffle(x)

list=x[0:10]


style= """<style>
h2{color:blue;}
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
"""
print style

print "<h2> Online Quiz </h2>"

print "<table>"
for i in range(0, len(list)):
   print "<tr>"
   print "<td>"
   print i
   print "</td>"
   print "<td>"
   print list[i]
   print "</td>"
   print "</tr>"

print "<table>"











