# 引入tkinter
import tkinter as tk
from tkinter import messagebox

from  tkinter  import ttk
import requests
import re

headers={

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    
}

login_url='http://xjw.sdau.edu.cn/jwglxt/xtgl/login_slogin.html?time=1611460078610'
grade_url='http://xjw.sdau.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=2019211551'
course_url='http://xjw.sdau.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151&su=2019211551'
# # 实例化tkinter对象，创建主窗口
# window = tk.Tk()
# window.resizable(width=False, height=False)
# # 设置窗口的标题
# window.title("教务处获取课本和成绩")
# # 设置窗口的大小和窗口的起始位置 window.geometry("宽度x高度+距离屏幕左边缘距离+距离屏幕上边缘距离")
# window.geometry("600x400")
# # 将标签显示在屏幕，进入等待状态,准备响应用户发起的GUI事件。

# def show_listbox():
#     alist = ['python','tk','java','c++']

#     listbox = tk.Listbox(window)
#     # listbox创建的时候，是空的，需要逐行插入数据
#     for item in alist:
#         # 'end'的意思是从最后插入（也有其他插入方式）
#         listbox.insert('end',item) 
#     listbox.pack()
# pass

# #show_listbox()
session=requests.session()

#这是系统的登录界面
class Login(object):

    def __init__(self):
        # 创建主窗口,用于容纳其它组件

        
        self.login_data = {
                            'yhm': 'none',
                            'mm': 'none',
        }




        # self.usr_name='none'
        # self.usr_pwd='none'
        self.root = tk.Tk()
        # 给主窗口设置标题内容
        self.root.title("登录系统")
        self.root.geometry('400x200')
        self.root.resizable(width=False, height=False)
        #运行代码时记得添加一个gif图片文件，不然是会出错的
        # self.canvas = tk.Canvas(self.root, height=400, width=700)#创建画布
        # self.image_file = tk.PhotoImage(file="test.gif")#加载图片文件
        # self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上
        # self.canvas.pack(side='top')#放置画布（为上端）

        #创建一个`label`名为`账户: `
        self.label_account = tk.Label(self.root, text='账户: ')
        #创建一个`label`名为`密码: `
        self.label_password = tk.Label(self.root, text='密码: ')
        
        # 创建一个账号输入框,并设置尺寸
        self.input_account = tk.Entry(self.root, width=30)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tk.Entry(self.root, show='*',width=30)

        # 创建一个登录系统的按钮
        self.login_button = tk.Button(self.root, command = self.usr_login, text = "登录", width=10)
        # 创建一个注册系统的按钮
        # self.siginUp_button = tk.Button(self.root, command = self.siginUp_interface, text = "注册", width=10)

    # 完成布局
    def place(self):
        self.label_account.place(x=60, y= 50)
        self.label_password.place(x=60, y= 75)
        self.input_account.place(x=110, y=50)
        self.input_password.place(x=110, y=75)
        self.login_button.place(x=125, y=100)
        # self.siginUp_button.place(x=220, y=100)

    # 进入注册界面
    # def siginUp_interface(self):
        # self.root.destroy()
        # tk.messagebox.showinfo(title='测试系统', message='进入注册界面')
        #这里没有写具体逻辑，这里一般应用是链接一个数据库，插入用户信息，留做发散思维

    # # 进行登录信息验证
    # def backstage_interface(self):
    #   user = self.input_account.get().ljust(10," ")
    #   password = self.input_password.get().ljust(10," ")
    #   #获取录入的账号以及密码
    #   tk.messagebox.showinfo(title='测试系统', message='录入账户:{}\n密码：{}\n登录成功！'.format(user,password))
    #   #这里没有写验证逻辑，读者可以发散思维，自己增加验证逻辑，例如自己设置一个固定的密码，然后判断；也可以读取数据库内容，做出各种判断

    def usr_login(self):
        usr_name = self.input_account.get()
        usr_pwd = self.input_password.get()
        self.login_data['yhm']=usr_name
        self.login_data['mm']=usr_pwd

        # self.session=requests.session()
        tk.messagebox.showinfo(title="查询中", message="查询您是否有权限使用" + usr_name)
        response = session.get('http://www.yh-sec.cc/user.html',headers=headers)

        user=re.findall('<=(.*?)=>',response.text)
        
        status=False
        for i in range(len(user)):
            if (usr_name == user[i]):
                status=True
                tk.messagebox.showinfo(title="结果", message="验证通过，正在检查密码" + usr_name)

        response = session.post(login_url,headers=headers,data=self.login_data)

        if (status == True) and (response.text.find('学籍异动申请')!=(-1)):
            tk.messagebox.showinfo(title="Welcome", message="How are you! " + usr_name)
            self.root.destroy()

            window_sign_up = first()
            window_sign_up.place()
            
        else:
            tk.messagebox.showinfo(title="error", message="what's wrong with you! " + usr_name)
                


           

class first(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件

        self.course_data={
                'xqm':'none',
                'xnm':'none'
        }

        self.grade_data={
                        'doType':'query',
                        'xqm':'none',
                        'xnm':'none',
}



        self.root = tk.Tk()
        # 给主窗口设置标题内容
        self.root.title("main系统")
        self.root.geometry('700x400')
        self.root.resizable(width=False, height=False)

        self.year='none'
        self.season='none'
        #创建一个`label`名为`账户: `
        self.label_account = tk.Label(self.root, text='年份: ')
        #创建一个`label`名为`密码: `
        self.label_password = tk.Label(self.root, text='学期: ')
        
        # 创建一个账号输入框,并设置尺寸
        self.input_account = tk.Entry(self.root, width=30)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tk.Entry(self.root, show='*',width=30)

        # 创建一个查询系统的按钮
        self.course_button = tk.Button(self.root, command = self.check_course, text = "查询课表", width=10)
        
        self.grade_button = tk.Button(self.root, command = self.check_grade, text = "查询成绩", width=10)


        self.year_value=tk.StringVar()#窗体自带的文本，新建一个值
        self.year_comboxlist=ttk.Combobox(self.root,textvariable=self.year_value) #初始化
        self.year_comboxlist["values"]=("2018","2019","2020","2021","2022")
        self.year_comboxlist.current(0)  #选择第一个
        
        self.year_comboxlist.bind("<<ComboboxSelected>>",self.get_year)  #绑定事件,(下拉列表框被选中时，绑定go()函数)

        self.season_value=tk.StringVar()#窗体自带的文本，新建一个值
        self.season_comboxlist=ttk.Combobox(self.root,textvariable=self.season_value) #初始化
        self.season_comboxlist["values"]=("3","12")
        self.season_comboxlist.current(0)  #选择第一个
        self.season_comboxlist.bind("<<ComboboxSelected>>",self.get_season)  #绑定事件,(下拉列表框被选中时，绑定go()函数)

    # 完成布局
    def place(self):
        self.label_account.place(x=60, y= 50)
        self.label_password.place(x=60, y= 75)
        self.year_comboxlist.place(x=110, y=50)
        self.season_comboxlist.place(x=110, y=75)
        self.grade_button.place(x=125, y=100)
        self.course_button.place(x=220, y=100)

    def get_year(self,*args):
        self.course_data['xnm']=self.year_comboxlist.get()
        self.grade_data['xnm']=self.year_comboxlist.get()
        print(self.course_data['xnm'])
    
    def get_season(self,*args):
        self.course_data['xqm']=self.season_comboxlist.get()
        self.grade_data['xnm']=self.year_comboxlist.get()
        print(self.course_data)
    
    def check_course(self):
        course_page = session.post(course_url,headers=headers,data=self.course_data)
        print(course_page.text)
    def check_grade(self):
        grade_page = session.post(grade_url,headers=headers,data=self.grade_data)
        print(grade_page.text)
        print('查询成绩')




def main():
    # 初始化对象
    L = Login()
    # 进行布局
    L.place()

    # 主程序执行
  
    tk.mainloop()


if __name__ == '__main__':
    main()



# window.mainloop()


