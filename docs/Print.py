import random
import urllib.request

filepath = 'myfile.txt'
list=[]
count=1
with open(filepath, 'r+', encoding="utf-8") as fp:
   line = fp.readline()
   print(line)  
   while line:
       list.append(line.strip())
       line = fp.readline()
       
random.shuffle(list)
my_range=list[0:10]
for x in range(0,10):
     print(my_range[x])
     count+=1

print("<tr>","<td>",count,"</td>","<td>",my_range[x],"</td><tr>")
