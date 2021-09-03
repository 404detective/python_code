import qrcode
# img = qrcode.make('https://blog.csdn.net/qq_26230027')
mystr = input("输入任意内容转换为二维码:")
img = qrcode.make(data=mystr)
img.show()
img.save('%s.png'%mystr)