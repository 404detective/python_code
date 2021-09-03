import requests
import re

login_url='http://xjw.sdau.edu.cn/jwglxt/xtgl/login_slogin.html?time=1611460078610'
grade_url='http://xjw.sdau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=2019211551'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',   }

grade_data_2019_3={'doType':'query','xqm':'3','xnm':'2019',}

login_data = {'yhm': '2019211551','mm': 'hsx13480933',}

session=requests.session()
response = session.post(login_url,headers=headers,data=login_data)

grade_page = session.post(grade_url,headers=headers,data=grade_data_2019_3)
  
course=re.findall('"kcmc":"(.*?)",',grade_page.text)

credit=re.findall('"xf":"(.*?)",',grade_page.text)

grade=re.findall('"cj":"(.*?)",',grade_page.text)

for i in range(len(course)):
        print ('课程:' +course[i]+' 学分:' +credit[i]+' 成绩:' +grade[i])
