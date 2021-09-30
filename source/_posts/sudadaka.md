---
title: 利用Python实现每日健康打卡
date: 2021-09-28 12:44:54
index_img: https://img.suxss.tk/common/daka-post1.webp
banner_img: https://img.suxss.tk/common/JKDKindex.jpg
excerpt: 学校要求每天都要健康打卡，于是做了个小爬虫自动化打卡
categories:
  - 爬虫
tags:
  - python
  - 爬虫
---

# 起因

学校要求每天都要健康打卡，每天都得填些一些固定的信息，感觉很繁琐，干脆写个爬虫。



# 抓包

先来抓包。由于是在手机app上打卡的，打卡所进行的网络请求不是直接暴露出来的，所以就先进行抓包。

## 1.HttpCanary

优先选黄鸟进行抓包，因为这个软件抓包的步骤没那么繁琐

首先，打开软件，在`设置-> 目标应用`中添加要抓包的app

然后点击抓包按钮，开始抓包

打开要抓包的app

然而，出现了类似于网络断开的现象，抓包失败

![黄鸟抓包失败](https://img.suxss.tk/common/daka-canary1.webp)

于是，更换抓包软件

## 2.Fiddler

打开电脑上的Fiddler，设置好手机网络，手动增加代理，主机名为`电脑ip` ， 端口号默认为`8888`

再次打开软件，成功抓包

![fiddler成功抓包](https://img.suxss.tk/common/daka-fiddler1.webp)

成功获取到打卡的网址：`http://dk.suda.edu.cn/default/work/suda/jkxxtb/`

有了这个，接下来的抓包工作就可以交给浏览器的开发者工具了

## 3.开发者工具

首先，用`selenium`库打开一个没有保存cookie的浏览器

发现要登录，利用抓包分析一下登录逻辑

结果发现登录还是比较简单的，主要就是网页里有几个隐藏元素，只需要解析网页源代码，提取出这几个值就好，其中只有id为`lt`和`pid`的元素的值是会变的，所以，只需要提取这两个值就好了

![所需隐藏元素](https://img.suxss.tk/common/daka-login1.webp)

拿到这些值，再加上密码和账号，做成一个字典，`post`到当前页面就能拿到cookie了

接下来就是挖掘如何提交健康信息的表单

为了方便测试，又不产生不必要的影响，先断网，以免发送了错误的数据

在网页代码中找到提交表单的业务代码段如下，打上断点

![开始调试](https://img.suxss.tk/common/daka-post1.webp)

先填好信息，然后点击提交开始调试

程序运行到断点停下来后，将要发送的信息提取出来

这里可以看到，要发送的信息在`data`中， 按照它的表达式在控制台中打印出信息

![截取data信息](https://img.suxss.tk/common/daka-post2.webp)

打印出来的信息就是到时候`post`的数据，而`post`的地址就是刚才断点附近的那个网址



# 代码
根据之前的结果就能写出所有的代码了
主要就是先访问目标网址，它会自动重定向到登录界面，
然后解析登录界面源代码，发送登录请求
接着带着cookie访问目标网址
最终发送post请求

<details>
<summary>完整代码</summary>
```python
import requests
import time
import re


username = ...  # 学号
password = ...  # 密码
url1 = 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/jkxxcj.jsp'
s = requests.session()
r1 = s.get(url1)
list_1 = re.findall(r'<input type="hidden" name="pid" value="(.*?)" />', r1.text)
list_2 = re.findall(r'<input type="hidden" name="lt" value="(.*?)">', r1.text)
login_data = {
    'username': username,
    'password': password,
    'pid': list_1[0],
    'lt': list_2[0],
    'source': 'cas',
    'execution': 'e1s1',
    '_eventId': 'submit'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
}
r2 = s.post(r1.url, data=login_data, headers=headers)
t = time.localtime()
t1 = time.strftime('%Y-%m-%d', t)
t2 = time.strftime('%Y-%m-%d %H:%M', t)
headers['Referer'] = r2.url
s.get(url='http://dk.suda.edu.cn/default/common/lib/mootools.js', headers=headers)  # 访问这个文件会多加一个cookie，至于有没有用我没有试
url = 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/com.sudytech.portalone.base.db.saveOrUpdate.biz.ext'
data = {'entity': {'sqrid': ...}}  # 刚才在控制台获取的信息
data['entity']['tbrq'] = t1
data['entity']['tjsj'] = t2

# print(data)
r = s.post(url, headers=headers, json=data)
print(r.json())

```
</details>




# 最后

每天运行这个程序就好了

如果想要更方便的话，可以将代码部署到云端，比如腾讯云函数或者服务器上，设置好每天运行一次就行了



