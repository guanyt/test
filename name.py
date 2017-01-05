#coding=utf-8  
import os
import os.path 

spath="temp.txt"
line_t=[]
name=[]
f=open(spath,"r") # Opens file for reading
for line in f:  
    index=line.find("http")
    if(index):      
        line_t.append(line[index:].replace("\t\n","").strip())
        name.append(line[:index].replace(":",",").replace("\t","").strip())  
f.close() 

rootdir = 'F:\cs50'   

for parent, dirnames, filenames in os.walk(rootdir):
	for dirname in dirnames:
		print("parent is: " + parent)
		print("dirname is: " + dirname)
	for filename in filenames:
		print("parent is: " + parent)
		print("filename is: " + filename)
		if(filename.find("课件")!=-1):
			print(filename)
			os.rename(os.path.join(parent, filename), os.path.join(parent, "课件.rar"))
		# for index in range(len(line_t)):
			# if(line_t[index].find(filename)!=-1):
				# newName=name[index]+".flv" 
				# print(filename, "---->", newName)
				# os.rename(os.path.join(parent, filename), os.path.join(parent, newName))
				# break
        #print ("the full name of the file is: " + os.path.join(parent,filename))  

os.system("pause")    
