#*--coding:utf-8--*

from bs4 import BeautifulSoup
import urllib2
from codecs import open as copen
import re

f=copen('naverReviewId.txt','a','utf-8')

li=[]
count=1
for i in range(1010,2000):
    count+=1
    if count%50==0:
        print count
    html = urllib2.urlopen('http://movie.naver.com/movie/point/af/list.nhn?&page='+str(i))
    soup = BeautifulSoup(html.read(), 'html.parser')
    title = soup.find_all('td',class_='ac num')
    for i in title:
        f.write(i.getText()+'\n')
f.close()

