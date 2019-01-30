# -*- coding: utf-8 -*-

from decorator import contextmanager
from pymysql import Error, connect, Connection
from pymysql.cursors import Cursor


@contextmanager
def get_cursor():
    cursor, conn = [None, None]
    try:
        conn = connect(host="192.168.163.1", port=3306, database="python_study", user="python",
                               password="python", charset="utf8")
    except Exception as e:
        print(e)
    else:
        cursor = conn.cursor()
        yield cursor

        try:
            conn.commit()
        except Error as e:
            conn.rollback()
            raise
    finally:
        if isinstance(cursor, Cursor):
            cursor.close()
        if isinstance(conn, Connection):
            conn.close()


def main():
    with get_cursor() as cursor:
        ret = cursor.execute("select * from users")
        print(ret)
        print(cursor.fetchall())


if __name__ == '__main__':
    main()
