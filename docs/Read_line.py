print("Content-type:text/html")
print()
filepath = 'C:\test\myfile.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
	   line = fp.readline()
       cnt += 1
	   