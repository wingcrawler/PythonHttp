# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:17:21 2013
@author: Leniy
"""
import os, base64

leniystr = "iVBORw0KGgoAAAANSUhEUgAAACwAAAAOCAYAAABU4P48AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAGYktHRAD/AP8A/6C9p5MAAAF6SURBVEhL1ZY9coMwEIWfchZIkckJxAmAhoojiNJu3KV0lwZK+xRU6ATmBJkUEXdRVj8MmGFsk9ge+5vReFlb2of0diymCTwRL0CHKmJgjKGQPnszJAqqw1iEqvOphZDgexJjRweq9QGrwKcWcmfB/+cCwf0xDiMan2dXIZp870ZBM6ecsIQs7Lzx2rLwa428ekawKZBgTxEvFbQqwSlu1+G830VDx61Qmh/RrO0So8YZBH2060//ohK1KUyILHYBcVqwrK1YgxHJwjVa//z1MxUj0OzMwgFe311mGTEyo5gq1kZxX5uX2Ax6L/QwTVK2WYZxmHYNf0Pow78SO8XYk2Lpt5fnKW3BwGWC228oH8756mrEG2enfYLEbS/y9HhjTgvuF6DDSaIKHTXYdsZX1yNAmtuCDp5jovfcDgdYHTQa1w0IrYc5SqVh7XoDgjS3jW0QH6sjO1jMX/NDoUpNgum6IHTjU2MeSLDSZD9zr7FDzKklnuzyA/wCcpDKoLig94YAAAAASUVORK5CYII="
imgData = base64.b64decode(leniystr)
leniyimg = open('imgout.png', 'wb')
leniyimg.write(imgData)
leniyimg.close()

