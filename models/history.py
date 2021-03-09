#!/usr/bin/python3
from utils.db import Sqlite3
from const import *
import prettytable as pt

class History(object):

    def __init__(self):
        self.tablename = "recite_history"
        self.wordstable = "master_vocabulary"
        self.dbhelper = Sqlite3(DATABASE)

    def addRecord(self, key, right):
        if key == "":
            return
        if right not in [WORD_RIGHT_YES, WORD_RIGHT_NO]:
            return
        sql = "insert into {}(key, right) values(?, ?)".format(self.tablename)
        self.dbhelper.execute(sql, (key, right))

    def findWrongWords(self, day=0):
        if day > 0:
            print("wrong=N, N can not be great than Zero")
            return
        start, end = "{}".format(day), "{}".format(day + 1)
        if day == 0:
            start, end = "-{}".format(day), "+{}".format(day + 1)
        sql = """
                select
                    count(*), mv.key, mv.desc
                from {} as rh
                join {} as mv
                on 
                    mv.key=rh.key
                    and
                    rh.daytime>=datetime('now','start of day','{} day') and rh.daytime<datetime('now','start of day','{} day')
                    and
                    rh.right=0 
                group by
                     mv.key
                """.format(self.tablename, self.wordstable, start, end)
        # print(sql)
        rows = self.dbhelper.fetch(sql, ())
        if rows is not None and len(rows) <= 0:
            print("no recite history.")
            return
        return rows

    def outputWrongWords(self, day=0):
        rows = self.findWrongWords(day)
        if rows is None or len(rows) <= 0:
            print("no wrong words history")
            return
        table = pt.PrettyTable(["Count", "Word", "Description"])
        for row in rows:
            if len(row) != 3:
                continue
            table.add_row([row[0], row[1], row[2]])
        print(table)



    def statics(self, day=0):
        day = int(day)
        if int(day) > 0:
            print("Unsupport static, please specify the number of N less then 0")
            return
        start, end = "{}".format(day-1), "{}".format(day)
        if day == 0:
            start, end = "-{}".format(day), "+{}".format(day+1)
        sql = """
        select
            mv.key, mv.desc, count(rh.right) as cnt
        from {} as rh
        join {} as mv
        on 
            mv.key=rh.key
            and
            rh.daytime>=datetime('now','start of day','{} day') and rh.daytime<datetime('now','start of day','{} day')
        group by
             mv.key
        order by cnt desc
        """.format(self.tablename, self.wordstable, start, end)
        # print(sql)
        rows = self.dbhelper.fetch(sql, ())
        if len(rows) <= 0:
            print("no recite history.")
            return
        table = pt.PrettyTable(["Count", "Word", "Description"])
        for row in rows:
            if len(row) != 3:
                continue
            table.add_row([row[2], row[0], row[1]])
        print(table)