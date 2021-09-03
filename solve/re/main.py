import re

with open('re.txt','r',encoding='utf-8') as f:
    string=(f.read())
    #print(txt)
course=re.findall('kcmc">(.*?)</td>',string)
#print ('课程为 ' ,course)
credit=re.findall('xf">(.*?)</td>',string)
#print ('学分为 ' ,credit)
grade=re.findall('tabGrid_cj">(.*?)</td>',string)
#print ('成绩为 ' ,grade)


for i in range(len(course)):
    print ('课程:' +course[i]+' 学分:' +credit[i]+' 成绩:' +grade[i])

    