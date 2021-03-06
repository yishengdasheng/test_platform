#!/usr/bin/env python
# -*- coding:utf8 -*-

import time, datetime
import hashlib


class Expandfunction:
    def __init__(self):
        pass

    # 获取当前时间(2019-03-12)/(2019-03)

    def getNowTime(self, format="%Y-%m-%d"):
        return time.strftime(format, time.localtime(time.time()))

    # 获取当前时间往前推一个月,日期固定为1(2019-02-01)
    # @staticmethod
    def getLastMonthTime(format="%Y-%m-%d"):
        today = datetime.date.today()
        first = today.replace(day=1)
        two = first - datetime.timedelta(days=1)
        lastMonth = two.replace(day=1)
        return lastMonth
        # return time.strftime(format, time.localtime(time.time()))

    #获取上一个月的最后一天
    # @staticmethod
    def getLastMonthDay(slef):
        last = datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(1)
        return last

    #设置固定时间等待
    def wait_time(self,seconds):
        time.sleep(seconds)
        return ""

    #获取几天后的那天开始的时间戳
    # @staticmethod
    def get_start_Timestamp(self, day):
        today = datetime.date.today()
        thatday = today + datetime.timedelta(days=day)
        thatday_start_time = str(int(time.mktime(time.strptime(str(thatday), '%Y-%m-%d')))) + "000"
        return thatday_start_time

    # 获取今天的时间，将其转换成时间戳

    def get_today_Timestamp(self):
        today = datetime.date.today()
        today_Timestamp = str(int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))) + "000"
        return today_Timestamp

    # 获取今天的日期数字（只要日期）
    # @staticmethod
    def get_today(self):
        today = datetime.date.today()
        day = today.day
        return day

    #获取昨天的日期数字(12)
    # @staticmethod
    def get_yestoday(self):
        today = datetime.date.today()
        day = today.day
        yestoday = int(day) - 1
        return yestoday

    # 获取明天的日期数字(11)
    # @staticmethod
    def get_tomorrow(self):
        today = datetime.date.today()
        day = today.day
        tomorrow  = day + 1
        return tomorrow



    # 获取当天时间，精确到秒（2019-03-19 00:00:00）
    def gettodaytime(self):
        day = str(self.getNowTime()) +" " + "00:00:00"
        return day

    # 获取今天往后推day(变量)天的日期数字（2019-03-19）
    def getafterday(self,day):
        today = datetime.date.today()
        thatday = today + datetime.timedelta(days=day)
        return thatday


    # 获取今天往后推3天的日期数字
    def getaftertoday3time(self):
        today = datetime.date.today()
        day = today.day
        afterday = day  +3
        return afterday

    # sha256加密
    @staticmethod
    def jm_sha256(value):
        '''
            sha256加密
              return:加密结果转成16进制字符串形式
        '''

        hsobj = hashlib.sha256()
        hsobj.update(value.encode("utf-8"))
        return hsobj.hexdigest()

    # 获取上个月的月份
    def last_month(self):
        today = datetime.datetime.today()
        month = today.month - 1
        return month



# if __name__ == '__main__':
    # e = Expandfunction()
    # # t = e.get_today_Timestamp()
    # # print(t)
    # g = e.getNowTime("%Y-%m-%d")
    # print(type(g))
    # w = e.getNowTime("%Y-%m")
    # print(w)
    # l = e.getLastMonthTime()
    # print(l)
    # d = e.get_today()
    # print(d)
    # y = e.get_yestoday()
    # print(y)
    # last = datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(1)
    # print(last)
    # k = e.gettodaytime()
    # print(k)
    # a = e.getaftertoday3time()
    # print(a)






