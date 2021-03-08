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
        key = str(key).lstrip("*")
        if right not in [WORD_RIGHT_YES, WORD_RIGHT_NO]:
            return
        sql = "insert into {}(key, right) values(?, ?)".format(self.tablename)
        self.dbhelper.execute(sql, (key, right))

    def findWrongWords(self):
        sql = """
                select
                    1, mv.key, mv.desc
                from {} as rh
                join {} as mv
                on 
                    mv.key=rh.key
                    and
                    rh.daytime>=datetime('now','start of day','-0 day') and rh.daytime<datetime('now','start of day','+1 day') 
                group by
                     mv.key
                """.format(self.tablename, self.wordstable)
        rows = self.dbhelper.fetch(sql, ())
        if len(rows) <= 0:
            print("no recite history.")
            return
        return rows



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
            mv.key, mv.desc, count(*) as cnt
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