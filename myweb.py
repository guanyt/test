#coding=utf-8 
import sys,urllib.request

url="http://www.snwx.com/book/77/77835/" #��ҳ��ַ
#url=sys.argv[1]
wp=urllib.request.urlopen(url)#������
content = wp.read() #��ȡҳ������

fp = open("web.txt","wb") #��һ���ı��ļ�
fp.write(content) #д������
fp.close() #�ر��ļ�


fp = open("web.txt","r")
for line in fp:
	if(line.find("<dt>")!=-1):
		filename=line[5:-9]+".txt"
		fs = open(filename,"wb")
		print(filename)
	if(line.find("<dd><a")!=-1):
		title=url+line[line.find("href=")+6:line.find("title")-2]
		print(title)
		wp=wp=urllib.request.urlopen(title)#������
		content = wp.read() #��ȡҳ������
		fs.write(content) #д������
fp.close() #�ر��ļ�
fs.close()
