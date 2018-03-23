# coding=UTF-8
from bs4 import BeautifulSoup
import urllib2
import re


class LianJiaParser(object):
    def __init__(self):
        self.index = 1

    def do_parser(self, url, region_id):
        if url == None:
            print("url 为空")
            return
        # 加载网页
        # request = urllib2.Request("https://nj.lianjia.com/ershoufang/gulou/")
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        res = response.read()

        # 解析页面
        soup = BeautifulSoup(res, 'html.parser', from_encoding="UTF-8")

        # 查找链接
        # tag_h2 = soup.find("h2", class_="total fl")
        # print("总房源:%s" % str(tag_h2.span.get_text()))
        # 房源列表li标签
        tag_li = soup.find_all("li", class_="clear")
        list = []
        for li in tag_li:
            sell_info = {}
            sell_info["detail_url"] = li.a["href"]  # 详情url
            # 房源信息
            for item in li.find("div", class_="info clear").children:
                itemClassName = item["class"][0]
                if itemClassName == "title":
                    sell_info["title"] = item.get_text()
                if itemClassName == "address":
                    sell_info["region"] = item.get_text()
                    sell_info["house_info"] = item.a.get_text()
                if itemClassName == "flood":
                    sell_info["flood"] = item.div.get_text()
                    sell_info["position_info"] = item.a.get_text()
                if itemClassName == "followInfo":
                    sell_info["follow_info"] = item.get_text()
                if itemClassName == "tag":
                    sell_info["tag"] = item.get_text()
                if itemClassName == "priceInfo":
                    sell_info["total_price"] = item.div.span.get_text()
                    sell_info["unit_price"] = item.find("div", class_="unitPrice")["data-price"]
            sell_info["region_id"] = region_id
            list.append(sell_info)
            # print(sell_info.get("title"))
            # print(sell_info.get("region"))
            # print(sell_info.get("house_info"))
            # print(sell_info.get("flood"))
            # print(sell_info.get("position_info"))
            # print(sell_info.get("follow_info"))
            # print(sell_info.get("tag"))
            # print(sell_info.get("total_price"))
            # print(sell_info.get("unit_price"))
            # print(sell_info.get("detail_url"))
            print("===========================", self.index)
            self.index += 1
        # print(len(list))
        return list
