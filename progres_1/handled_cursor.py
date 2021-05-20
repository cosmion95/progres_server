import cx_Oracle
from django.db import connection
import sys

def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
    if defaultType == cx_Oracle.DB_TYPE_CLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
    if defaultType == cx_Oracle.DB_TYPE_BLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)

class HandledCursor:
    def __init__(self):
        self.cursor = connection.cursor()

    def callproc(self, proc_name, parameters):
        self.cursor.callproc(proc_name, parameters)

    def callfunc(self, func_name, return_type, parameters):
        function_return_value = self.cursor.callfunc(func_name, return_type, parameters)
        return function_return_value

    def clobFunction(self, func_name, parameters):
        select = "select " + func_name + "("
        paramValues = {}
        for i in range(len(parameters)):
            select = select + ":" + str(i) + ", "
            paramValues[str(i)] = parameters[i]
        select = select[0: (len(select)-2)] + ") from dual"
        connection.outputtypehandler = OutputTypeHandler
        cursor = connection.cursor()
        cursor.execute(select, paramValues)
        clob = cursor.fetchone()
        return str(clob[0])

