#*--coding:utf-8--*

from bs4 import BeautifulSoup
import urllib2
from codecs import open as copen
import re
import pickle

f=copen('naverReviewId.txt','r','utf-8')

result={}
count=1
for i in f.readlines():
    temp={}
    t=[]
    index=0
    count+=1
    if count%50==0:
        print count
    html = urllib2.urlopen('http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword='+i.replace('\n','')+'&target=after')
    soup = BeautifulSoup(html.read(), 'html.parser')
    title = soup.find_all('td',class_='title')
    score = soup.find_all('td',class_='point')
    
    for j in title:
        t.append(j.find(class_='movie').getText().replace('\r\n',''))

    for j in score:
        temp[t[index]]=j.getText()
        index+=1

    result[i]=temp

print result

with open('reviewData.txt','wb') as p:
    pickle.dump(result,p)
        
f.close()

