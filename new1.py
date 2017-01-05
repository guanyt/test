import re
spath="temp.txt"
line_t=[]
name=[]
f=open(spath,"r") # Opens file for reading
for line in f:	
	index=line.find("http")
	if(index):		
		line_t.append(line[index:].replace("\t\n","").strip())
		rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
		line = re.sub(rstr,",", line)
		name.append(line[:index].replace("\t","").strip())	
f.close()
f=open("2.txt","w")
for line in name:
	f.writelines(line+"\n")	
	print(line)
f.close()
# curDir = rootdir
# print(curDir)
# oldId = "jisuanjikexuecs50"  
# newId = "CS50"  
# for parent, dirnames, filenames in os.walk(curDir):    
    # for filename in filenames:  
        # if filename.find(oldId)!=-1:  
            # newName = filename.replace(oldId, newId)  
            # print(filename, "---->", newName)  
            # os.rename(os.path.join(parent, filename), os.path.join(parent, newName))  