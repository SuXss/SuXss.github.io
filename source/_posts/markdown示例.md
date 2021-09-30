---
title: markdown示例
index_img: https://cdn.jsdelivr.net/gh/suxss/image/2021/1.png
banner_img: 'https://cdn.jsdelivr.net/gh/suxss/image/wallroom-3840x2160-bg-8c6afe1.jpg'
math: true
excerpt: 这是一个示例文件
categories:
  - 测试
tags:
  - python
  - c
date: 2021-08-06 17:14:00
mathjax: true
---

## 表格

|| 周一 | 周二 | 周三 |
|---| ---- | ---- | ---- |
|上午|睡觉|睡觉|睡觉|
|下午|睡觉|睡觉|睡觉|
|晚上|打豆豆|打豆豆|打豆豆|

## 代码

``` python
import scrapy
import json
from weixindata.items import WeixindataItem


class TeamdataSpider(scrapy.Spider):
    name = 'teamdata'
    start_urls = [
        'https://algo.weixin.qq.com/wealgo-bin/leaderboard/get_all_leaderboard?page_index=1&page_size=10']

    def parse(self, response):
        re = json.loads(response.text)
        item = WeixindataItem()
        page = int(response.url.split('&')[-2].split('=')[-1])
        list_1 = [
            '那么多C带带我怎么了',
            '吃得粮中粮，方为狗中皇',
            '在马里亚纳海沟里学深度学习',
            '平安喜乐',
            'R&Q',
            '苏大启航队',
            'HelloWorld',
            '乐乐乐',
            'long_bo_heng',
            'Krista八千鸟',
            '今晚海底捞',
            '诺飞扬',
            'twohzre小队',
            'jokers',
            '摸鱼划水']
        for i in re['data']['detail']:
            if i['team_name'] in list_1:
                item['team_name'] = i['team_name']
                item['team_seq'] = i['seq']
                item['team_score'] = i['score']
                yield item
        print(page)
        if page < 146:
            yield scrapy.Request(
                url='https://algo.weixin.qq.com/wealgo-bin/leaderboard/get_all_leaderboard?page_index=' + str(
                    page + 1) + '&page_size=10')

```



## 公式

$$
\begin{aligned}
b_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,dx \\
\frac{\pi^2}{6}&=\sum_{n=1}^\infty{\frac{1}{n^2}}
\end{aligned}
$$



## 图片

![图片1](https://cdn.jsdelivr.net/gh/suxss/image/wallroom-2880x1800-bg-f296f86.jpg)



## 列表

1. 吃饭
2. 睡觉
3. 打豆豆



## 标签

{% note info %}

关于我打豆豆这档事

{% endnote %}

{% note danger %}

打豆豆很危险

{% endnote %}



## 音乐

<div style=" display:flex;justify-content: center;"><iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=26908739&auto=0&height=66"></iframe>
</div>



## 视频

{% dplayer "url=https://vodkgeyttp8.vod.126.net/cloudmusic/MDBhYjEzNDAiMSVhMmAwIA==/mv/5360055/1a5361fe29672813e3b85e565eafb685.mp4?wsSecret=e517badf76196044be5dd475fe20bce0&wsTime=1629194829" "pic=" "loop=yes" "theme=#FADFA3" "autoplay=false" "token=tokendemo" %}

