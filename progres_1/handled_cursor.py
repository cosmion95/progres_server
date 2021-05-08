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

    def clobFunction(self, judet):
        connection.outputtypehandler = OutputTypeHandler
        cursor = connection.cursor()
        cursor.execute("select nomenclatoare.get_localitati(:judet) from dual", {'judet': judet})
        clob = cursor.fetchone()
        return str(clob[0])

