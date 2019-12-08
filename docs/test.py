Options +ExecCGI 
AddHandler cgi-script .py

#!/usr/bin/python 
import random
print "Content-type: text/html\n" 

print ("Hi")
