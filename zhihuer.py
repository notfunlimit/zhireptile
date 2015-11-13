import re
from urllib.request import *
import requests

question_id='27647963'

s = requests.session()
h = s.get('http://www.zhihu.com/question/'+question_id)
html= h.content

zan_like=r'<span class="count">[0-9]*</span>'
zanlist=re.findall(zan_like,html.decode())

question_r=r'href="/question/[0-9]*/answer/[0-9]*">'
quelist=re.findall(question_r,html.decode())

for i in range(0,len(quelist)):
	#pass
	likelist=list(zanlist[i])[20:-7]
	queslist=list(quelist[i])[6:-2]
	print('zhihu.com'+''.join(queslist))
	print('Like:'+''.join(likelist))
