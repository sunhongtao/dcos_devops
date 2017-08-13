#encoding:utf-8

import pymysql


def execute_sql(sql_info):
    db = pymysql.connect(host="192.168.0.102", user="root",
                         password="root", db="alert_info", port=3366,charset="utf8")
    cur = db.cursor()
    try:
        cur.execute(sql_info)
        result = cur.fetchall()
    except Exception as e:
        raise e
    finally:
        db.close()
    return result