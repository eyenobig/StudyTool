import os
import json
resjson = []
for parent,dirnames,filenames in os.walk(os.getcwd()):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

    for filename in filenames:                        #输出文件信息
        if filename[-3:] == 'txt':
            file = os.path.join(parent,filename)
            for line in open(file,"rb"):
                first = line.decode("utf-8").strip('\n').split(";")
                if first[0] == 'LANGUAGE_NAME_NATIVE':
                    settings = []
                    settings.append("[" + first[1].strip() + "]")
                    xjson = {}
                    xjson['Language'] =  first[1].strip()
                    yjson = {}
                    for x in open(file,"rb"):
                        result = x.decode("utf-8").strip('\n').split(";")
                        if result[0] == 'TOOLTIP_RANGED_ATTACK':
                            title = result[1].split("</b>")
                            resstr = "{ranged_attack} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['ranged_attack'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_CHARGE':
                            title = result[1].split("</b>")
                            resstr = "{charge|} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['charge'] = title[0].replace("<color=white>","")[:-1] + "</b>"


                        if result[0] == 'TOOLTIP_GIFT':
                            title = result[1].split("</b>")
                            resstr = "{gift} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['gift'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_PRODUCTION':
                            title = result[1].split("</b>")
                            resstr = "{production} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['production'] = title[0].replace("<color=white>","")[:-1] + "</b>"


                        if result[0] == 'TOOLTIP_COMBAT':
                            title = result[1].split("</b>")
                            resstr = "{combat} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['combat'] = title[0].replace("<color=white>","")[:-1] + "</b>"


                        if result[0] == 'TOOLTIP_PROTECTION':
                            title = result[1].split("</b>")
                            resstr = "{protection} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['protection'] = title[0].replace("<color=white>","")[:-1] + "</b>"


                        if result[0] == 'TOOLTIP_TAUNT':
                            title = result[1].split("</b>")
                            resstr = "{taunt} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['taunt'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_HASTE':
                            title = result[1].split("</b>")
                            resstr = "{haste} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['haste'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_LAST_WORDS':
                            title = result[1].split("</b>")
                            resstr = "{last_words} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['last_words'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_DEATHTOUCH':
                            title = result[1].split("</b>")
                            resstr = "{deathtouch} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['deathtouch'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_AQUATIC':
                            title = result[1].split("</b>")
                            resstr = "{aquatic} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['aquatic'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_JUMP':
                            title = result[1].split("</b>")
                            resstr = "{jump} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['jump'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_FLYING':
                            title = result[1].split("</b>")
                            resstr = "{flying} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['flying'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_ACTIVATE':
                            title = result[1].split("</b>")
                            resstr = "{activate} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['activate'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        if result[0] == 'TOOLTIP_OPTIONS':
                            title = result[1].split("</b>")
                            resstr = "{options} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                            settings.append(resstr)
                            yjson['options'] = title[0].replace("<color=white>","")[:-1] + "</b>"

                        # if result[0] == 'TOOLTIP_FAERIA':
                        #     title = result[1].split("</b>")
                        #     resstr = "{faeria} =" + title[0].replace("<color=white>","")[:-1] + "</b>"
                        #     settings.append(resstr)
                        #
                    xjson['config'] = yjson
                    # print(yjson)
                    resjson.append(xjson)
                    with open("Language.txt", "a" , encoding='utf-8') as f:
                        for each_setting in settings:
                            f.write(each_setting + '\n')
# print(resjson)
with open("jsonlang.txt", "w" , encoding='utf-8') as f:
    f.write(str(resjson).replace("'",'"'))
