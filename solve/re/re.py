import re
# string = "hello world! I'm glad to see you here. This is 404detecitve. 你好，世界！我很高兴在这见到你。"
# replacedString = re.sub(r'[\W]', " ", string)

# replacedString = re.sub(r'[\u4e00-\u9fa5,]', "", string)
# print("replacedString = ", replacedString) 


# string = '''<aa>12<b>23<c>34<d><e\n>
# 12<
# f>23<g>34<h>'''

# No_S = re.findall(r'[\d]',string)
# Yes_S = re.findall(r'<(.*?)>',string,re.S)
# print ('No_re.S is ' ,No_S)
# print ('Yes_re.S is ' ,Yes_S)



import re

with open('re.txt','r',encoding='utf-8') as f:
    string=(f.read())
    #print(txt)
course=re.findall('kcmc">(.*?)</td>',string)
print ('课程为 ' ,course)
credit=re.findall('xf">(.*?)</td>',string)
print ('学分为 ' ,credit)
grade=re.findall('cj">(.*?)</td>',string)
print ('成绩为 ' ,grade)






# def readhtmlfile(filename):
#     f = open(filename,encoding='utf-8')
#     html = ''
#     while True:
#         tmp = f.read(1)
#         if tmp == '':
#             break
#         html += tmp
#     return html

#txt=readhtmlfile('re.txt')
#print(txt)