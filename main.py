import requests
import re
import tujidao


# 功能测试 下载 搜索结果页下的 全部图片
# tuji_url 配置为图集岛搜索得到的 搜索结果页
# 使用该功能 请注意 检查cookie是否可用
"""
name = "铃木爱理"
tuji_url = "https://tujidao06.com/t/?id=1817"
cookie = '__51vcke__Je64MI06Q1Neac4F=c8a64275-05e9-5400-a69b-a729f1e572a9; __51vuft__Je64MI06Q1Neac4F=1684810716297; PHPSESSID=09pund3eb1s8260vpp23sh6c39; __51uvsct__Je64MI06Q1Neac4F=4; uid=403547; name=WatchDemo; leixing=0; __vtins__Je64MI06Q1Neac4F={"sid": "93d9d142-473c-5348-9fb1-ef7276dd7d37", "vd": 31, "stt": 914573, "dr": 10623, "expires": 1684834497705, "ct": 1684832697705}'
tujidao.downloadPage(name, tuji_url, newCookie=cookie)
"""

# 功能测试 单组图片下载
"""
tujidao.downloadFolder("Airi Suzuki Vol.124","https://tjgew6d4ew.82pic.com/a/1/8529/1.jpg")
"""

# 功能测试 单个图片下载
"""
A = "https://tjgew6d4ew.82pic.com/a/1/8528/0.jpg"
B = "https://tujidao06.com/"
tujidao.downloadSigle("demo.jpg", A, B)
"""