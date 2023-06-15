import requests
import os
import re
import time


def downloadSigle(file_path, pic_url, refererUrl="https://tujidao06.com/"):
    # 一个非常基本地下载图片所需的函数 基于规则下载页面的全部图片 直至返回404 提示全部下载完毕
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        "Referer": refererUrl}
    MaxRetryTime = 0

    while MaxRetryTime < 24:
        try:
            r = requests.get(pic_url, headers=headers)
            break
        except requests.exceptions.ConnectionError:
            print("****Warning**** 下载过快", MaxRetryTime, " 秒后重试 ****Warning****")
            MaxRetryTime = MaxRetryTime + 1
            time.sleep(MaxRetryTime * 5)

    if MaxRetryTime == 24:
        print("****Error**** 下载过快 多次重试 故障未解除 ****Error****")
        print("****Error**** 下载过快 多次重试 故障未解除 ****Error****")
        print("****Error**** 下载过快 多次重试 故障未解除 ****Error****")
        time.sleep(1440)
        return 404

    if r.status_code != 404:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    else:
        print("All done")

    return r.status_code


def titleFix(string):
    # 本函数的目的是修复通过正则表达式提取的标题
    index = string.find(">")
    if index != -1:
        return string[index + 1:]
    else:
        return string


def downloadFolder(folderName, start_url, base="D:/TujiDownload/"):
    # 本函数用于下载 链接形如 https://tjgew6d4ew.82pic.com/a/1/8501/0.jpg 的图片
    # 图片存储的位置是 D:/TujiDownload/ + folderName
    # 如果该位置已经存在该文件夹 则跳过下载的过程
    folderName = base + folderName + "/"
    print(folderName)
    folderExists = os.path.exists(folderName)
    if not folderExists:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(folderName)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("****Start****", folderName, " downloading", "****Start****")
    else:
        print("****Pass****", folderName, "has been downloaded befor", "****Pass****")
        return 0
    print(start_url)
    start_url = start_url[:-5]
    picIndex = 1
    while downloadSigle(folderName + str(picIndex) + ".jpg", start_url + str(picIndex) + ".jpg") != 404:
        # print(folderName, picIndex)
        picIndex = picIndex + 1
    print("****Note****", folderName, "has been downloaded successfully", "****Note****")
    time.sleep(1)


def downloadPage(name, tuji_url, newCookie='', page=1, base="D:/TujiDownload/"):
    # 本函数旨在下载一个类目下的全部图片，并归档 搜索功能需要提供cookie，但无需开通会员
    # 例如：https://tujidao06.com/t/?id=1817 指向铃木爱理全部图集
    headers = {
        # 假装自己是浏览器
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        # 把你刚刚拿到的Cookie塞进来
        'Cookie': newCookie}
    session = requests.Session()
    # 分情况处理搜索结果的首页和后续页
    if page == 1:
        print("Start working on page ", tuji_url)
        response = session.get(tuji_url, headers=headers)
    else:
        print("Start working on page ", tuji_url + "&page=" + str(page))
        response = session.get(tuji_url + "&page=" + str(page), headers=headers)
    textReturn = response.text
    # 利用正则表达式处理搜索返回的网页
    patternPicUrl = r"https://.*?\.jpg"
    patternTitle = r'<p class="biaoti">(.*?)</a></p>'
    matchesPicUrl = re.findall(patternPicUrl, textReturn)
    matchesTitle = re.findall(patternTitle, textReturn)
    successTarget = 0
    print(matchesTitle)
    print(matchesPicUrl)
    # 返回的页面图片数量可能和标题数量不一致，因为部分页面会有模特的介绍图，所以此处用 matchMagicNumber 进行修正
    matchMagicNumber = len(matchesPicUrl) - len(matchesTitle)
    print("debug matchMagicNumber", matchMagicNumber)
    # 依次调用downloadFolder函数逐个下载返回的页面
    for i in range(0, len(matchesTitle)):
        try:
            matchesTitle[i] = titleFix(matchesTitle[i])
            print(matchesTitle[i], matchesPicUrl[i + matchMagicNumber])
            successTarget = successTarget + 1
        except IndexError:
            print("--------------IndexError in matchesPicUrl--------------")
            break
        downloadFolder(name + "/" + matchesTitle[i], matchesPicUrl[i + matchMagicNumber], base=base)
    if successTarget > 0:
        print("-------page ", page, "find target=", successTarget, "-------")
        downloadPage(name, tuji_url, newCookie=newCookie, page=page + 1, base=base)
