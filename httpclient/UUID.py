# -*- coding: utf-8 -*-

import uuid

name = "test_name"
namespace = "test_namespace"
filePath = "file/"
filePath2 = "file/"

py = uuid.uuid1()
print uuid.uuid1()  # 带参的方法参见Python Doc
print uuid.uuid3(uuid.NAMESPACE_DNS, name)
print uuid.uuid4()
print uuid.uuid5(uuid.NAMESPACE_DNS, name)

filePath.join(str(uuid.uuid1()))
filePath2 = filePath2 + str(uuid.uuid1())

print filePath
print filePath2
