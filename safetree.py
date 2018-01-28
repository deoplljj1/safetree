#encoding:utf8
import urllib2
import cookielib
import requests
import csv
csvFile = open("stu.csv", "r")
reader = csv.reader(csvFile)
for itema in reader:
   ls=1;
   name=''
   account=''
   for item in itema:
     if ls==1:
        ls=ls+1
        name=item
     else:
        account=item
   print 'Now working for '+name+' --------OK.'
   cookie = cookielib.CookieJar()
   handler = urllib2.HTTPCookieProcessor(cookie)
   opener = urllib2.build_opener(handler)
   res1 = opener.open('https://fujianlogin.safetree.com.cn/LoginHandler.ashx?jsoncallback=jQuery16101399218103949702_1517066657599&userName='+account+'&password=123456&checkcode=&type=login&loginType=1&r=0.15874360017266986&_=1517066672454')
   for cok in cookie:
        print 'Name:'+cok.name+'Val:'+cok.value
   res1=requests.get("https://longyan.safetree.com.cn/Topic/topic/platformapi/api/v2/Holiday/sign?callback=jQuery11130018805381389931597_1517063229057&schoolYear=2018&semester=1&step=1&specialId=132&prvName=&cityName=&_=1517063229059",cookies=cookie)
   d = {'schoolYear': '2018', 'semester': '1' , 'step' : '2'}
   res2= requests.post('https://longyan.safetree.com.cn/Topic/topic/platformapi/api/v1/holiday/sign',data=d,cookies=cookie)
   print res2.content
#print(data)
csvFile.close()
