# -*- coding:utf-8 -*-
# Author : Niuli
# Data : 2018/11/19 上午9:40

# pip install pillow
# pip install numpy
# pip install imageio
# pip install myqr



# version, level, qr_name = myqr.run(
#     words='dhb cdfb64%vjk',  # 不支持中文，支持 0~9,a~z, A~Z 以及常见的常用英文标点符号和空格
#     version=2,  # 版本，从 1至 40
#     level='H',  # 纠错等级，范围是L、M、Q、H，从左到右依次升高
#     picture='4e.jpg',  # 文件要放在目录下
#     colorized=True,   # True 为彩色，False 为黑白
#     contrast=1.0,  # 对比度
#     brightness=1.0,  # 亮度
#     save_name='1d6.bmp',  # 命名随便都行，格式可以是 jpg,png,bmp,gif
#     save_dir="F:\二维码"  # 路径要存在
# )



from MyQR import myqr

# 普通二维码
# myqr.run(words='should be str')
# myqr.run(words='xxxxx' ,picture='150*150.jpg')

# count = 0
# for i in range(1,40):
#     myqr.run(words='should be str',version=i,save_name='%s.jpg'%(count))
#     count+=1


# 动态彩色二维码
# 先找到一个new1.gif动图做背景,picture='new1.gif',
# 再设置为彩色:colorized=True
# myqr.run(words='this is colourful qrcode',picture='timg.gif',colorized=True,version=5)
myqr.run(words='http://niuli.xyz',picture='timg.gif',colorized=True,version=5)


