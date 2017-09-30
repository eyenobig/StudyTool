# -*- coding:utf-8  -*-

import os
import os.path
import sqlite3

cx = sqlite3.connect(os.getcwd() + "\MushroomDx.sqlite")
cu = cx.cursor()

# 装备表
def Squotes(data):
    strtest = ""
    # print(data)
    if data.find('"') == -1:
        strtest =  '"' + data + '"'
    else:
        strtest = data
    return strtest
def InsertData(Tname,Tdata):
    Insertsql = "insert into "+Tname+" VALUES ("
    for x in Tdata:
        # print(x)
        if x:
            Insertsql += Squotes(x) + ","
        else:
            Insertsql += "'" + "null" + "',"
    Insertsql = Insertsql[:-1]+ ")"
    print(Insertsql)
    cu.execute(Insertsql)
    cx.commit()
def equip_creatre():
    tablesql = "create table equip ('ID','test1','test2','test3','test4','test5','japanese','english','chinese','korean')"
    cu.execute(tablesql)
    cx.commit()
    with open('equip_table.txt', 'rb') as f:
        for v in f:
            data = v.strip().split(',')
            InsertData('equip',data)

def nameko_creatre():
    tablesql = "create table nameko ('ID','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10','test11','test12','test13','test14','test15','test16','test17','test18','test19','test20')"
    cu.execute(tablesql)
    cx.commit()
    with open('nameko_table.txt', 'rb') as f:
        i = 1
        test = 0
        for v in f:
            # v = v.replace('"',"<br>")
            upload = []
            Tem = ''
            data = v.strip().split(',')
            print(data[10])
            # if data[12].find('\\n') >= 0:
            #     if test - i > 1:
            #         print("不存在")
            #     test = i
            # for x in data:
            #     if x.find('"') >= 0 or x.find("'") >= 0:
            #         Tem += x

            #     else:
            #         if Tem:
            #             upload.append(Tem)
            #             Tem = ''
            #         upload.append(x)
            # if len(upload) == 22:
            #     print(upload)
            # print(type(data))
            # if Tem:
            #     print("123")
                # if x.find('"'):
                #     data[i]
            # InsertData('nameko',data)

            # print(upload)
            # if len(data) == 21:
            #     print(v.strip())
            # if i == 1:
            #     data = v.strip().split(',')
            #     print(data)
            #     print(len(data))
            i += 1
            # data = v.strip().split(',')


def putout():
    # equip_creatre()
    nameko_creatre()
def init():
    try:
        putout()
    except sqlite3.OperationalError:
        # cu.execute("DROP TABLE equip")
        cu.execute("DROP TABLE nameko")
        cx.commit()
        putout()

init()
