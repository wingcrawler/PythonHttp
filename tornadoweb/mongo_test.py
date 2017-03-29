# -*- coding: utf-8 -*-
"""
author = 'luthais'
"""

# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'bitfeng'
# Define your db_connect here


from pymongo import MongoClient
import re
import datetime


# mongdb数据库链接
class MongoDBConnect(object):

    def __init__(self, mongodb_uri):
        try:
            self.host = mongodb_uri['host']
            self.port = mongodb_uri['port']
            self.database = mongodb_uri['database']
            self.user_name = mongodb_uri['user_name']

            self.conn = self.createConn(mongodb_uri)
        except Exception as e:
            print(str(e))

    def clean_dict(self, data_dict):
        if isinstance(data_dict, dict):
            for k, v in data_dict.items():
                if not v:
                    data_dict.pop(k)
                else:
                    if '.' in k:
                        data_dict[re.sub('\.', '~', k)] = data_dict.pop(k)
                    self.clean_dict(v)
        elif isinstance(data_dict, list):
            for var in data_dict:
                self.clean_dict(var)
        # else:
        #     print 'clean_dict error: %s not a list or dict' % to_str(data_dict)
        return data_dict

    def insert(self, col, data):
        if isinstance(data, dict):
            try:
                self.conn[self.database][col].insert_one(data)
            except Exception as e:
                print('insert_one error ' + str(e))
        elif isinstance(data, list):
            try:
                self.conn[self.database][col].insert_many([var for var in data])
            except Exception as e:
                print('insert_many error ' + str(e))
        else:
            print('data is not a dict or a list of dicts')

    def update(self, col, data, filter, upsert=True):
        update_results = []
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, (dict, str, unicode, datetime.datetime)):
                    modify = '$set'
                    modify_data = {k: v}
                elif isinstance(v, (list, tuple, set)):
                    modify = '$push'
                    modify_data = {k: {'$each': list(v)}}
                else:
                    print("the type of data[%s] is an wrong when updating mongodb" % k)
                    break
                try:
                    update_result = self.conn[self.database][col].update_one(
                        filter=filter,
                        update={modify: modify_data},
                        upsert=upsert
                    )
                    if update_result.matched_count > 0:
                        update_results.append(update_result)
                except Exception as e:
                    print('update data error:' + str(e))
            return update_results
        else:
            print ('data is not a dict or a list of dicts')

    def find_one(self, col, filter={}):
        return self.find(col , filter)

    def find(self, col, filter={}):
        if isinstance(filter, dict):
            try:
                return self.conn[self.database][col].find_one(filter)
            except Exception as e:
                print(str(e))
        return

    def find_cursor(self, col, filter={}):
        if isinstance(filter, dict):
            try:
                return self.conn[self.database][col].find(filter)
            except Exception as e:
                print(str(e))
        return

    @classmethod
    def createConn(cls, mongodb_uri):
        try:
            conn = MongoClient(
                host=mongodb_uri['host'],
                port=mongodb_uri['port'],
            )
            db = conn[mongodb_uri['database']]
            db.authenticate(name=mongodb_uri['user_name'], password=mongodb_uri['password'])
            return conn
        except:
            print('Mongo connected Fail!')

    def close(self):
        self.conn.close()