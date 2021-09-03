from pymouse import PyMouse 
import time
# 初始化鼠标对象
m = PyMouse()

# 移动鼠标到（x，y）绝对地址
#m.move(200 ,200)

# 鼠标中键垂直滚动 10 个单位
#m.scroll(10 ,0)
#print(m.position())
def get_position():
    for i in range(50):
        x=m.position()[0]
        y=m.position()[1]
        print(x,y)
        time.sleep(1)

#print(m.position()[0])
def click():
    for i in range(200000):
        x=m.position()[0]
        y=m.position()[1]
    # 鼠标点击（500，300），第三个参数代表键位，1是左键，2是右键，3是中键
        m.click(x,y,1)
        time.sleep(1)

def click_all():
    all_position=(114,154,133,254,128,827,131,646)
    for i in range(2000000):
        x=all_position[0]
        y=all_position[1]
        m.click(x,y,1)
        x=all_position[2]
        y=all_position[3]
        m.click(x,y,1)
        x=all_position[4]
        y=all_position[5]
        m.click(x,y,1)
        x=all_position[6]
        y=all_position[7]
        m.click(x,y,1)
        time.sleep(2)
click_all()

#get_position()






# 鼠标从当前位置拖拽到（500 ， 300）
#m.drag(500 , 300)

# 获得当前屏幕大小
#m.screen_size()

# 获得鼠标当前位置

