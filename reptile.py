import re
from urllib.request import *
import requests
import sys
import os
import webbrowser
	
loc=os.getcwd()

#print(title)
def getans():

	question_id=input('Question id:')
	s = requests.session()
	h = s.get('http://www.zhihu.com/question/'+str(question_id)+'?all')
	html= h.content


	zan_like=r'<span class="count">[0-9]*</span>'
	zanlist=re.findall(zan_like,html.decode())
	#<a href="/question/20899988/answer/24692816" class="toggle-expand">
	#question_r=r'<*href="/question/[0-9]*/answer/[0-9]*">'
	question_r=r'target="_blank" href="/question/[0-9]*/answer/[0-9]*">'
	quelist=re.findall(question_r,html.decode())

	file=open(str(question_id)+'.html','w')

	for i in range(0,len(quelist)):
		#pass
		likelist=list(zanlist[i])[20:-7]
		queslist=list(quelist[i])[22:-2]
		
		file.write('<a href="http://zhihu.com'+''.join(queslist)+'">'+'\n')		
		file.write(str(i+1)+': Like:'+''.join(likelist)+'<br>\n')
	file.close()
	webbrowser.open(loc+'/'+str(question_id)+'.html')


getans()
