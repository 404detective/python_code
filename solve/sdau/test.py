import smtplib
import requests
from email.mime.text import MIMEText
import time
from bs4 import BeautifulSoup as bs
import urllib3
import urllib.request

session = requests.session()
login_url='http://xjw.sdau.edu.cn/jwglxt/xtgl/login_slogin.html?time=1611460078610'
course_url='http://xjw.sdau.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N2151&layout=default&su=2019211551'
select_url='http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=2019211551'
grade_url='http://xjw.sdau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=2019211551'
download_url='http://xjw.sdau.edu.cn/jwglxt/kbcx/xskbcx_cxXsShcPdf.html?doType=table'
headers={

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'referer':'http://xjw.sdau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=2019211551'
}

grade_data={
    'doType':'query',
    'gnmkdm':'N305005',
    'su':'2019211551',
    'queryModel.sortName':'',
    'queryModel.currentPage':'1',
    'xqm':'12',
    'queryModel.showCount':'15',
    'nd':'1611843651691',
    'time':'2',
    'xnm':'2019',
    'queryModel.sortOrder':'asc',
    '_search':'false',


}
login_data = {
    'yhm': '2019211551',
    'mm': 'hsx13480933',

}

s=requests.session()
response = s.post(login_url,headers=headers,data=login_data)
#print(response.text)



page = s.post(grade_url,headers=headers,data=grade_data)
#weatherHtml = urllib.request.urlopen(login_url,data=login_data)
#weatherHtml = urllib.request.urlopen(grade_url)
print(page.text)



f=open('a.txt','w',encoding='utf-8')
f.write(page.text)

#html = session.post(grade_url,headers=headers)


#soup = BeautifulSoup(html.content)
#soup = bs(html.text, 'lxml')

#page = requests.get(url,headers=headers)
#print(soup.body['id'='bodyContainer'])
#soup.body['id'='bodyContainer']

#print(soup.body.find(id="bodyContainer").find(id="yhgnPage").find(id='innerContainer'))
#for child in soup.descendants:
    #print(child)
#time.sleep(2)