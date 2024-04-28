# 图集岛图集批量下载程序说明

本项目旨在编写一个能批量下载图集岛指定人物全部图片的程序。
Cookie需要自行填写，无需购买付费VIP，免费账号即可。

+ 核心代码为tujidao.py
+ 测试样例见main.py

## 全类目下载

`downloadPage(name, tuji_url, newCookie='', page=1, base="D:/TujiDownload/")` 

该函数可以下载一个类目下的全部图片，并归档。
+ name 为在base目录下创建文件夹的名称。
+ tuji_url 为图集岛的默认链接。
  + 使用图集岛的查找功能需要注册，然后填写Cookie,否则无法访问搜索结果页。
  + 例如 铃木爱理图集的地址为 https://www.tujidao06.com/t/?id=1817 填写Cookie后才能正常访问。
+ page 指定了下载开始的页面，默认为从第一页开始下载
+ base 指定了下载后存储位置，默认为 *D:/TujiDownload/*

## 单个图集页下载

`downloadFolder(folderName, start_url, base="D:/TujiDownload/")`

该函数可以下载指定单个图集页。
+ folderName 为在base目录下创建文件夹的名称。
+ start_url 为封面图片 0.jpg 的地址，具体解释如下。

还是以铃木爱理图集为例。铃木爱理图集【 https://www.tujidao06.com/t/?id=1817 】如图。 

<img src="https://picy.itrefer.com/2023/05/24_%E6%88%AA%E5%B1%8F2023-05-24%2013.25.11.png" alt="图集岛 铃木爱理" style="zoom:67%;" />

如果需要下载第一个图集 *[Young Gangan] 2017年No.07* ，那么复制该封面图片的地址填入`start_url`。 
对于本案例应为【 https://tjgew6d4ew.82pic.com/a/1/30817/0.jpg 】。

<img src="https://picy.itrefer.com/2023/05/24_0-20230524133055544.jpg" alt="封面图像地址" style="zoom:100%;" />

## 单个图片下载
`downloadSigle(file_path, pic_url, refererUrl="https://tujidao06.com/")`
在下载图片，例如【 https://tjgew6d4ew.82pic.com/a/1/30817/0.jpg 】时，需要填写一个refererUrl才能正确下载。
这个地址可能会有变动，如果后期观察到变动比较频繁，可能会考虑给`downloadFolder`和`downloadPage`函数添加`refererUrl`参数。
