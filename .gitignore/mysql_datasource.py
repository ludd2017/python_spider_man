# coding=utf-8
import pymysql


class DataSource(object):
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(host="localhost", user="root",
                                  password="123456", db="spider_man", port=3306, charset='utf8')

    def add(self, list):
        # 使用cursor()方法获取操作游标
        cur = self.db.cursor()

        sql_insert = "insert into ershoufang_lianjian ( title, region_id, house_info, flood,position_info,follow_info,tag,total_price, unit_price, detail_url,create_time) values"

        str_temp = ""
        for info in list:
            str_temp = "('" + info.get("title") + "','" + str(info.get("region_id")) + "','" + info.get(
                "house_info") + "','" \
                       + info.get("flood") + "','" \
                       + info.get("position_info") + "','" + info.get("follow_info") + "','" + info.get("tag") + "','" \
                       + str(info.get("total_price")) + "','" + str(info.get("unit_price")) + "','" + info.get(
                "detail_url") \
                       + "', now()),"
            sql_insert += str_temp
        try:
            cur.execute(sql_insert.rstrip(","))
            # 提交
            self.db.commit()
            print("添加成功")
        except Exception as e:
            # 错误回滚
            print(e)
            self.db.rollback()
            self.db.close()

    def closeCon(self):
        self.db.close()
        print("关闭资源")
