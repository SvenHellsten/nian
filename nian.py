import requests
import re
import json
from bs4 import BeautifulSoup

ord=[]
for x in range(1, 44):
	page = requests.get('http://spraakdata.gu.se/saolhist/lista_ord_bok.php?p='+str(x)+'&submitbn=lista_ord_bok.php&fr=a&limit=5000&med=SAOL14&inte=tom&finns=SAOL14&lemma=%25&inte_alla=OFF&endast_olika=OFF&order=0&mode=SAOLprod&urval=0')
	print('Getting page: http://spraakdata.gu.se/saolhist/lista_ord_bok.php?p='+str(x)+'&submitbn=lista_ord_bok.php&fr=a&limit=5000&med=SAOL14&inte=tom&finns=SAOL14&lemma=%25&inte_alla=OFF&endast_olika=OFF&order=0&mode=SAOLprod&urval=0')
	soup = BeautifulSoup(page.content, 'html.parser')
	# print([type(item) for item in list(soup.children)])
	l =soup.find_all('a')
	for s in l: 
		su=s.get_text()
		if ((su !="(Dölj)") and (su!='Visa alla rader')):
			o = re.sub('[-|]', '', su)
			if len(o)==9 and ' ' not in o:
				print(o)
				ord.append(o)
	print('page' +str(x)+ 'of 43 done')

with open('your_file.txt', 'w') as f:
	json.dump(ord,f)
f.close()