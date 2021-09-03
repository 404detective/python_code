import requests
import re

login_url='http://xjw.sdau.edu.cn/jwglxt/xtgl/login_slogin.html?time=1611460078610'
#course_url='http://xjw.sdau.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N2151&layout=default&su=2019211551'
course_url='http://xjw.sdau.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151&su=2019211551'
select_url='http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=2019211551'
grade_url='http://xjw.sdau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=2019211551'
download_url='http://xjw.sdau.edu.cn/jwglxt/kbcx/xskbcx_cxXsShcPdf.html?doType=table'

catch_url='http://xjw.sdau.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=2019211551'

headers={

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    #'referer':'http://xjw.sdau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=2019211551'
}

grade_data_2019_3={
    'doType':'query',
   
    'xqm':'3',
    'xnm':'2019',
}

grade_data_2019_12={
    'doType':'query',
   
    'xqm':'12',
    'xnm':'2019',
}

grade_data_2020_3={
    'doType':'query',
   
    'xqm':'3',
    'xnm':'2020',
}

grade_data_2020_12={
    'doType':'query', 
    'xqm':'12',
    'xnm':'2020',
}

course_data_2020_3={

    'xqm':'3',
    'xnm':'2020'

}

login_data = {
    'yhm': '2019211551',
    'mm': 'hsx13480933',

}

catch_data_wangqiu={
    # 'gnmkdm':'N253512',
    # 'su':'2019211551',
    # 'rlkz':'0',

    'qz':'0',

    # 'rlzlkz':'0',
    # 'cxbj':'0',

    # 'sxbj':'0',
    # 'xxkbj':'0',

    # 'xklc':'1',

    # 'kcmc':'(XT108007)网球 - 1 学分',
    # 'jxb_ids':'1847b48931ba151f0faf042e58a3f5fbfac5a0031e956a96bfd779d4e09ca0fc274a4d209559232ebb46d017dd9da2cd7db6126460c6a0d99e5188bfc4e2286ea6e53df27448a2e0e2eb9e8b54a08fee50db7d90b096c7330c24a31bf7e74928d020a738669c5e7499c56d84ad460d478c2b69a7517e9f701ad99e6d893f4799',
    'jxb_ids':'35174300a38b1caec2f3967e5d0facfe6713910a9339f9788b7b7169963c0c7b06e6d4fc41a8a32975943aa2edd49774bf273ce66500021c60fead51f0ae2c24a545bb48a5f04efc7db21610164e5a73dce40d78a52edc09f2181844c87e86d3e7246c3033fd8c2688426b29d25dc532357730f2bf612299c9daa95d654ff0de',
    
    #'xkkz_id':'B9385FD794433D63E0536785C2CAABB7',

    'kch_id':'XT108007',

    # 'xkxnm':'2020',
    # 'njdm_id':'2019',
    # 'rwlx':'2',
    # 'xkxqm':'12',
    # 'kklxdm':'15',
    # 'zyh_id':'058',
}

catch_data_pingpang={
    'qz':'0',
    'jxb_ids':'2529887c30c8ab33e7d30e86c4b74f8bbe884f2293d6962608783cf637aa002ffe2df43d666a20f5452bbcc920c1177952d13c1e20701ff5b0decde5c3516decaecae9d233b8cc4553c4754b2fcb0fccad0989a1690a8e54ce9af507fe91e8870169ecb4ec37e7a1e2fb3c48efabe050d4047dd80bb581a1add4ee51b8621fb3',
    'kch_id':'XT108005',
}

catch_data_xiandai={
    'qz':'0',
    'jxb_ids':'090d6878b97ff8154cd31a98edfaf67ccc09080ead3a14f30fc80f172cbd34f5833ee28d08ac119d7fab6e136df2a2b894c3b58ee25c42b3d79c23d13a36f94c88e11d2638f51ea3622f78bcc752ad1bbee6d1419e284f03f5f949409522aa7637c5e03e24c0abca77ff0dd4c1ef1b2b29fc30af75d7778e52fa51932fc81941',
    'kch_id':'96A66B5EA69BC886E0536685C2CAF0D8',
}

catch_data_xinli={
    'qz':'0',
    'jxb_ids':'5f3043e39119889d52b49128197bf04c6c3563ebe97042377bbaee46e4072d7ce0116af7860bf98562ba48761efad5f5d90b3eab4218b721affda64722b8c7236da8c2309495d8da172dd95fdc5a22c69c38d9f121b2c8669d50c78f5df47d84caad5b373c194ca67ea6d6f77319507d5d73fdbe4c370457032a2ae732365a14',
    'kch_id':'XK038003',
}

catch_data_meixue={
    'qz':'0',
    'jxb_ids':'52eb9f44c5587417c709551410eaa2d3b6774a2b59a893acde087ba01f9a6fcda786aa57d6ea4dec463ec8c28b03d946390953c21ee38ca4fb5aabebc9c31ff2d32cb431d8b805443faad56aaddee2407218b870bb72955fc3c4dbf666c70ca1e6b554695e047ddc83a697b1d9951969f326ca1448cbb4a0a91573bffc99a1f1',
    'kch_id':'XY153001',
}

catch_data_yumaoqiu={
    'qz':'0',
    'jxb_ids':'54802260d1e14a59a1fd77f362b8f9af29f8fae1d0641316ab68fa895c33056ef805c591952980dd78fe68c4bc5e3f01d2f1c65cd5c1b117008a0f9fb6bde8c905a9e622f87ca4b94412385c6e907816d7946ed7f3211b060f6ebacfda00eb790d2590e92eebc940fe564b7657248f323a0b7a1d39f2848d85f22dc6f10eec86',
    'kch_id':'XT108006',
}

session=requests.session()
response = session.post(login_url,headers=headers,data=login_data)

response = session.post(catch_url,headers=headers,data=catch_data_pingpang)

print(response.text)

response = session.post(catch_url,headers=headers,data=catch_data_xinli)

print(response.text)

response = session.post(catch_url,headers=headers,data=catch_data_xiandai)

print(response.text)

response = session.post(catch_url,headers=headers,data=catch_data_meixue)

print(response.text)

response = session.post(catch_url,headers=headers,data=catch_data_wangqiu)

print(response.text)

response = session.post(catch_url,headers=headers,data=catch_data_yumaoqiu)

print(response.text)


# course_page = session.post(course_url,headers=headers,data=course_data_2020_3)

# #print(course_page.text)

# course_page_text = re.sub('自动化(.*?)星期日', "xm", course_page.text)
# print(course_page.text)
# course=re.findall('"kcmc":"(.*?)",',course_page_text)
    
# teacher=re.findall('"xm":"(.*?)",',course_page_text)
    
# position=re.findall('"cdmc":"(.*?)",',course_page_text)

# time=re.findall('"xqjmc":"(.*?)",',course_page_text)

# time_2=re.findall('"jc":"(.*?)",',course_page_text)
    

# for i in range(len(course)):
#     print ('课程:' +course[i]+' 教师:' +teacher[i]+' 教室:' +position[i]+' 上课时间:'+time[i]+time_2[i])




# grade_page = session.post(grade_url,headers=headers,data=grade_data_2019_12)

# #print(grade_page.text)

# def print_grade():
#     xq=input('要查询的学期，格式2019上/下\n')
#     if(xq=='2019上'):
#         grade_page = session.post(grade_url,headers=headers,data=grade_data_2019_3)
#     elif(xq=='2019下'):
#             grade_page = session.post(grade_url,headers=headers,data=grade_data_2019_12)

#     course=re.findall('"kcmc":"(.*?)",',grade_page.text)
      
#     credit=re.findall('"xf":"(.*?)",',grade_page.text)
        
#     grade=re.findall('"cj":"(.*?)",',grade_page.text)
        

#     for i in range(len(course)):
#         print ('课程:' +course[i]+' 学分:' +credit[i]+' 成绩:' +grade[i])

# print_grade()


