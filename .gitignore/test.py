import url_manager
import lianjia_parser
import mysql_datasource


class Test(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    regionDict = {1: "gulou", 2: "jianye", 3: "qinhuai", 4: "xuanwu", 5: "yuhuatai", 6: "qixia", 7: "jiangning",
                  8: "pukou", 9: "liuhe", 10: "lishui", 11: "gaochun"}
    for region in regionDict:
        urls = url_manager.UrlManger().getLianJiaUrls(regionDict.get(region))
        ljParser = lianjia_parser.LianJiaParser()
        ds = mysql_datasource.DataSource()
        for url in urls:
            fangList = ljParser.do_parser(url, region)

            ds.add(fangList)

    ds.closeCon()
