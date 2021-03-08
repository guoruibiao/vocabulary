#!/usr/bin/python3
from utils.db import Sqlite3
from const import *

class Words(object):

    def __init__(self):
        self.tablename = "master_vocabulary"
        self.dbhelper = Sqlite3(DATABASE)

    def insert(self, key, desc):
        if key == "":
            return
        sql = "insert into {}(key, desc) values(?, ?)".format(self.tablename)
        self.dbhelper.execute(sql, (key, desc))

    def find(self, key):
        """
        method `find` can only return one record at most
        :param key:
        :return:
        """
        if key == "":
            return
        sql = "select * from {} where key='{}'".format(self.tablename, key)
        res = self.dbhelper.fetch(sql, ())
        if len(res) >= 1:
            return res[0]
        return res

    def findall(self):
        """there are 5k+ words at most, so it's easy to get all of them."""
        sql = "select * from {} ".format(self.tablename)
        resultSet = self.dbhelper.fetch(sql, ())
        return resultSet

    def updateDesc(self, key, desc):
        if key == "":
            return
        record = self.find(key)
        if record is not None:
            sql = "update {} set desc=? where key=?".format(self.tablename)
            self.dbhelper.execute(sql, (desc, key))
        else:
            self.insert(key, desc)

    def setAsCutoffed(self, key):
        if key == "":
            return
        record = self.find(key)
        if record[1] != key or record[3] != WORD_TYPE_CUTOFF:
            return
        sql = "update {} set cutoff={} where key=?".format(self.tablename, WORD_TYPE_CUTOFFED)
        self.dbhelper.execute(sql, (key,))

    def setAsUnCutoff(self, key):
        if key == "":
            return
        record = self.find(key)
        if record[1] != key or record[3] != WORD_TYPE_CUTOFFED:
            return
        sql = "update {} set cutoff={} where key=?".format(self.tablename, WORD_TYPE_CUTOFF)
        self.dbhelper.execute(sql, (key,))

    def importWords(self, rows):
        """
        import words to sqlite3-db
        :param rows: the format must be [('key', 'desc'), ...]
        :return:
        """
        for row in rows:
            self.insert(row[0], row[1])

    def exportAsCSV(self, filepath):
        pass