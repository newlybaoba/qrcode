最近经常听到网站编辑妹子嚷嚷着说公众号二维码太丑了, 想要个好看的,

‘要二维码? 找我啊, 我做二维码贼6!  PS, AI, Coredraw, 你说你想要哪种做?’

“Python吧..”

‘你妹的.. 以为这个能难倒我? 来来来, 叔叔教教你!  ‘

今天就讲讲python怎么搞二维码的事吧.


介绍一个好玩的库: qrcode

qrcode 运行在 Python 3 上，它可以生成以下三种二维码图片：普通二维码、带图片的艺术二维码（黑白与彩色）、动态二维码（黑白与彩色）。它比较适合直接用于生成二维码图片的场景。

安装 qrcode 库可以使用 pip 方式。但是该库依赖 pillow、numpy 和 imageio。因此，我们需要先安装依赖库，再安装 qrcode。最后的安装命令如下：

pip install pillow
pip install numpy
pip install imageio
pip install myqr
简单的解释下

数	含义	详细
words	二维码指向链接	str，输入链接或者句子作为参数
version	边长	int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级
level	纠错等级	str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为’H’
picture	结合图片	str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
colorized	颜色	bool，使产生的图片由黑白变为彩色的
contrast	对比度	float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
brightness	亮度	float，调节图片的亮度，其余用法和取值与 contrast 相同
save_name	输出文件名	str，默认输出文件名是”qrcode.png”
save_dir	存储位置	str，默认存储位置是当前目录
有40种样式吧,不过也就前面7种还行,后面的实在是,密集恐惧症莫入啊

废话不多说,直接上代码

-*- coding:utf-8 -*-
Author : Niuli

from MyQR import myqr

普通二维码
\# myqr.run(words='should be str')
\# myqr.run(words='xxxxx' ,picture='150*150.jpg')

\# 40个版本样子方便查看选择想要的
\# count = 0 
\# for i in range(1,40):
\#     myqr.run(words='should be str',version=i,save_name='%s.jpg'%(count))
\#     count+=1


\# 动态彩色二维码
\# 先找到一个new1.gif动图做背景,picture='new1.gif',
\# 再设置为彩色:colorized=True
\# myqr.run(words='this is colourful qrcode',picture='timg.gif',colorized=True,version=5)
myqr.run(words='http://niuli.xyz',picture='timg.gif',colorized=True,version=5)
最后,如果要自动跳转网址的话, 需要加上  word=’http://你的网址’

blob:http://niuli.xyz/f8318925-b6d1-4683-b634-c3e0d7a90157

最后..真正的二维码,,还是用作图软件做吧, 哈哈


