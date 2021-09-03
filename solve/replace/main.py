import re

f=open('1.txt',encoding='utf-8')
f_output=open('1_output.txt','w',encoding='utf-8')
a=f.readlines()
print(type(a))
labelsWord = []
for i in a:
    i_replacedStr = re.sub(r'[\u4e00-\u9fa5]', " ", i)
    #i_replacedStr = re.sub(r"[%s]+" %',()', " ", i_replacedStr)
    #i_replacedStr = re.sub(r'()', " ", i)
    #i_replacedStr = re.sub(r')', " ", i)
        #for iword in i_replacedStr:
            #if(i<'z'):
                #labelsWord += iword
    f_output.write(i_replacedStr)
    pass

                #print('labelsWord = ',labelsWord)




    #if(i):
        #print(type(i))

#if((i<'z') and (i>'a')):
#if((i>'a')&(i<'z')) .isalpha()
#print(repr(i.encode('utf-8')))