# -*- coding: utf-8 -*-

import os
import os.path
import sqlite3

cx = sqlite3.connect(os.getcwd() + "\Faeria.sqlite")
cu = cx.cursor()

def Creattable(Tname,Tdata):
    n = 0
    tablesql = "create table "+Tname+" ("
    for x in Tdata:
        tablesql += "name" + str(n) + ","
        n += 1
    tablesql = tablesql[:-1]+")"
    cu.execute(tablesql)
    cx.commit()

def InsertData(Tname,Tdata):
    Insertsql = "insert into "+Tname+" VALUES ("
    for x in Tdata:
        # print(x)
        if x:
            Insertsql += Squotes(x) + ","
        else:
            Insertsql += "'" + "null" + "',"
    Insertsql = Insertsql[:-1]+ ")"
    # print(Insertsql)
    cu.execute(Insertsql)
    cx.commit()
def Squotes(data):
    strtest = ""
    # print(data)
    if data.find("'") == -1:
        strtest =  "'" + data + "'"
    elif data.find('"') == -1:
        strtest =  '"' + data + '"'
    else:
        strtest = data

    return strtest

def DataCreat(file):
    for line in open(file):
        first = line.strip('\n')
        data = first.split(";")
        if data[0] == "1":
            try:
                Creattable("test",data)
                InsertData("test",data)
            except sqlite3.OperationalError:
                cu.execute("DROP TABLE test")
                cx.commit()
                Creattable("test",data)
                InsertData("test",data)
        else:
            InsertData("test",data)

def LangTable(lang):
    try:
        tablesql = "create table "+lang+" (id,name,text)"
        cu.execute(tablesql)
        cx.commit()
    except sqlite3.OperationalError:
        cu.execute("DROP TABLE " +lang)
        cx.commit()
        tablesql = "create table "+lang+" (id,name,text)"
        cu.execute(tablesql)
        cx.commit()

def LangCreat(file,lang):

    LangTable(lang)

    for line in open(file,"rb"):
        first = line.decode("utf-8").strip('\n').split(";")
        second = first[0].split(".")
        if second[1] == 'name':
            name = first[1]
        if second[1] == 'text':
            InsSql = "insert into " + lang + " ('id','name','text') VALUES (" + Squotes(second[0]) +","+Squotes(name)+","+Squotes(first[1])+")"
            print(InsSql)
            cu.execute(InsSql)
            cx.commit()



for parent,dirnames,filenames in os.walk(os.getcwd()):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

    for filename in filenames:                        #输出文件信息
        if filename[-3:] == 'csv':
            path = os.path.join(parent).split("\\");
            if path[-1] == "CardExport":
                DataCreat(os.path.join(parent,filename))
            else:
                LangCreat(os.path.join(parent,filename),path[-1])

cx.close()


