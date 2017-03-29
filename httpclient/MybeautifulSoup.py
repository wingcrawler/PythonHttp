#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


def parse_list(trinfo):
    # psoup = BeautifulSoup(trinfo, "xml")  # 指定文档解析器
    result = (
        trinfo.select('span')[0].get_text().strip(), trinfo.select('span')[1].get_text().strip(),
        trinfo.select('span')[2].get_text().strip()
        , trinfo.select('span')[3].get_text().strip(), trinfo.select('span')[4].get_text().strip(),
        trinfo.select('span')[5].get_text().strip()
        , trinfo.select('span')[6].get_text().strip(), trinfo.select('span')[7].get_text().strip());

    # result[1] = trinfo.select('span')[1].get_text().strip()
    # result[2] = trinfo.select('span')[2].get_text().strip()
    # result[3] = trinfo.select('span')[3].get_text().strip()
    # result[4] = trinfo.select('span')[4].get_text().strip()
    # result[5] = trinfo.select('span')[5].get_text().strip()
    # result[6] = trinfo.select('span')[6].get_text().strip()
    # result[7] = trinfo.select('span')[7].get_text().strip()

    return result


# doc = open('C:/Users/Administrator/Desktop/table.html', 'r')
# print doc.read()


def parse_table(doc):
    print type(doc)
    soup = BeautifulSoup(doc, "lxml")  # 指定文档解析器
    info = soup.select('table.table > tr')
    aList = [];
    for m in range(len(info)):
        # print type(info[m])
        aList.append(parse_list(info[m]));

        # print type(info[m].get_text().strip())
    return aList
