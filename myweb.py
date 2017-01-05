#coding=utf-8 
import sys,urllib.request

url="http://www.snwx.com/book/77/77835/" #网页地址
#url=sys.argv[1]
wp=urllib.request.urlopen(url)#打开连接
content = wp.read() #获取页面内容

fp = open("web.txt","wb") #打开一个文本文件
fp.write(content) #写入数据
fp.close() #关闭文件


fp = open("web.txt","r")
for line in fp:
	if(line.find("<dt>")!=-1):
		filename=line[5:-9]+".txt"
		fs = open(filename,"wb")
		print(filename)
	if(line.find("<dd><a")!=-1):
		title=url+line[line.find("href=")+6:line.find("title")-2]
		print(title)
		wp=wp=urllib.request.urlopen(title)#打开连接
		content = wp.read() #获取页面内容
		fs.write(content) #写入数据
fp.close() #关闭文件
fs.close()
