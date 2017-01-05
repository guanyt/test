#coding=utf-8 
import sys,urllib.request,re
if(len(sys.argv)-1):
	url=sys.argv[1]
else:
	print("please input url!")
	sys.exit()
	url="http://www.dhzw.com/book/89/89117/" #网页地址
wp=urllib.request.urlopen(url)#打开连接
content = wp.read().decode('ansi') #获取页面内容

name=re.search("<h1>(.*)</h1>",content)
if(name):
	filename=name.group(1)+".txt"
	print(filename)#文件名
	fs = open(filename,"w")
	page=re.findall('href="(.*)" title=.*>(.*)</a></dd>',content)#

	for temp in page:
		#print(temp[0])
		title=url+temp[0]#去掉 双引号(“”)
		wp=urllib.request.urlopen(title)#打开连接
		content = wp.read().decode('ansi') #获取页面内容
		data = re.search("<h1>(.*)</h1>[\s\S]*BookText.*>([\s\S]*)</div>[\s\S]*sharex",content)
		if(data):
			line=data.group(2)
			line=line.replace("<br /><br />","\n").replace("&nbsp;"," ")
			#print(title+"  "+data.group(1))
			fs.write(data.group(1)+line) #写入数据
	fs.close()
print("finish")