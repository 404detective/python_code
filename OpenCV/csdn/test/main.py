from cv2 import cv2
import matplotlib.pyplot as plt

def image_show():
    image = cv2.imread('tu.jpg')
    cv2.namedWindow("Image") # 初始化一个名为Image的窗口
    cv2.imshow("Image", image) # 显示图片
    cv2.waitKey(0) # 等待键盘触发事件，释放窗口
    pass
# openCV_image_show()

def image_pltshow():
    img = cv2.imread("tu.jpg")
    # print(img.shape)  # (301, 400, 3)
    # print(cv2.split(img))
    b, g, r = cv2.split(img)
    
    print(cv2.split(img))

    # print(b.shape)	#(301, 400)
    # 重组后的图片

    img2 = cv2.merge([r, g, b])
    plt.subplot(211)
    plt.xticks([])  # 隐藏x、y轴
    plt.yticks([])
    plt.imshow(img)

    plt.subplot(212)
    plt.xticks([])  # 隐藏x、y轴
    plt.yticks([])
    plt.imshow(img2)

    plt.show()

# image_show() 展示图片
# image_pltshow()  画板绘制