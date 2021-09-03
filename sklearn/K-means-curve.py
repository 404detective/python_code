import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def lodaData(filePath):
    f = open(filePath, 'rb')
    data = []
    img = Image.open(f)
    m, n = img.size
    for i in range(m):
        for j in range(n):
            x, y, z ,a= map(lambda x:x/256.0, img.getpixel((i, j)))
            data.append([x, y, z])
            
    f.close()
 
    return np.mat(data), m, n
 
 
imgData, row, col = lodaData("E://Desktop//python_code//sklearn//课程数据//基于聚类的整图分割//person.png")
print(imgData)
# 图片当中的颜色（包括背景共有）3类
km = KMeans(n_clusters=3)
# 聚类获得每个像素所属的类别
label = km.fit_predict(imgData)
label = label.reshape([row, col])
# 创建一张新的灰度图以保存聚类后的结果
pic_new = Image.new("RGB", (row, col))
# 根据类别向图片中添加像素值
for i in range(row):
    for j in range(col):
        # 如果属于背景的类别，填充红色
        if label[i][j] == 0:
            pic_new.putpixel((i, j), (255, 0, 0))
        # 输入白色的牛角和文本类别，填充绿色
        elif label[i][j] == 1:
            pic_new.putpixel((i, j), (0, 255, 0))
        # 属于第三类的牛头类别填充蓝色
        else:
            pic_new.putpixel((i, j), (0, 0, 255))
# 以JPEG格式保存图像
pic_new.save("E:\Desktop\python_code\sklearn\课程数据\基于聚类的整图分割\\person3.png", "PNG")






# # -*- coding: utf-8 -*-
# import numpy as np
# import PIL.Image as image
# from sklearn.cluster import KMeans

# def loadData(filePath):
#     f = open(filePath,'rb')#以二进制形式读取文件
#     data = []
#     img = image.open(f)
#     m,n = img.size
#     #将每个像素点的RGB归一化并存入data
#     for i in range(m):
#         for j in range(n):
#             x,y,z = img.getpixel((i,j))
#             data.append([x/256.0,y/256.0,z/256.0])
#     f.close()
#     return np.mat(data),m,n

# imgData,row,col = loadData('E://Desktop//python_code//sklearn//课程数据//基于聚类的整图分割//bull.jpg')
# #聚类获取每个像素点的类别
# label = KMeans(n_clusters=4).fit_predict(imgData)
# label = label.reshape([row,col])

# #创建一张新的灰度图保存聚类后的结果
# pic_new = image.new("L", (row, col))

# #根据所属类别向图片中添加灰度值
# for i in range(row):
#     for j in range(col):
#         pic_new.putpixel((i,j), int(256/(label[i][j]+1)))

# #以JPEG形式保存图像
# pic_new.save("E://Desktop//python_code//sklearn//课程数据//基于聚类的整图分割//result-bull-44.jpg", "JPEG")
