#!/usr/bin/python3

import sqlite3


class Sqlite3(object):
    """
    sqlite3 helper
    """

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.ddlKeywords = ["create", "update", "delete", "insert"]

    def execute(self, sql, params):
        """
        execute the sql statement expect `select`
        :param sql:   specific sql statement, example: update table set property1=? where property2=?
        :param params: the format is tuple.   example: (paramter1, parameter2)
        :return: True/False
        """
        succ = False
        try:
            cursor = self.conn.cursor()
            if cursor is None:
                return
            cursor.execute(sql, params)
            # ddl should be committed to database
            if str(sql[:6]).lower() in self.ddlKeywords:
                self.conn.commit()
                succ = True
        except Exception as e:
            print(e)
            self.conn.rollback()

        return succ

    def fetch(self, sql, params):
        """
        the result set of `select` sql statement.
        :param sql:  specific sql statement, example: select * from table where property1=?
        :param params: (parameter1,)
        :return: [(), ...]
        """
        resultSet = []
        try:
            cursor = self.conn.cursor()
            if cursor is None:
                return
            cursor = cursor.execute(sql, params)
            resultSet = cursor.fetchall()
        except Exception as e:
            print(e)
            # self.conn.rollback() # only ddl should be committed or rollback
        return resultSet

    def getConn(self, db=""):
        """
        get the database connection of `db`
        :param db: string
        :return:
        """
        return self.conn if self.conn is not None else sqlite3.connect(db)

    def releaseConn(self):
        try:
            if self.conn is not None:
                self.conn.close()
                self.conn = None
        except Exception as e:
            print(e)