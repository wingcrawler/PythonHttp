# encoding=utf-8
import MySQLdb


# try:
#     conn = MySQLdb.connect(host='localhost', user='root', passwd='tai@123', db='zjcredit', port=3306, charset='utf8')
#     cur = conn.cursor()
#
#     count = cur.execute('select * from result_new')
#     print 'there has %s rows record' % count
#
#     result = cur.fetchone()
#     data = cur.fetchall()
#     for i in data:
#         print 'id: %s \t %s' % (i[5], i[4])
#
#     # print 'tobacco_user: %s info %s' % result
#     cur.close()
#     conn.close()
# except MySQLdb.Error, e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# 插入一条数据
def insert(resultList):
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='tai@123', db='tobacco_crawl', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        # sqli = "insert into webapp_task_result (order_num, order_status,order_date,\
        #  oder_species, order_total,order_sell, order_sum) values ( '% s', '% s', '% s', '% s', '% s', '% s', '% s')" % \
        #        ('312312432', '完结', '2015-02-15', '7', '5', '12', '12345.2')

        sqli = "insert into webapp_task_result (order_num, order_status,order_date, oder_species,\
     order_total,order_sell, order_sum,order_pay) values (% s, % s, % s, % s, % s, % s, % s ,% s)"
        # cur.execute(sqli, ('312312433', '完结', '2015-02-16', '22', '5', '12', '12545.2'))
        #    cur.execute(sqli)

        cur.executemany(sqli, resultList)
        cur.close()
        conn.commit()
        conn.close()

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
