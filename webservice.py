#!/usr/bin/python2.7

import web
import datetime
import platform
import config
import pytz
import time


urls = (
    '/(.*)', 'temps'
)
app = web.application(urls, globals())
now = time.localtime()
dist = platform.linux_distribution()[0]
release = platform.linux_distribution()[1]
#timezone = pytz.timezone(config.Default_Timezone)
print time.strftime('Nous sommes en %Y, et il est %H:%M.',time.localtime()) 


class temps:
    def GET(self, temps):
                 return time.strftime('Nous sommes: en %Y, et il est %H:%M:%S', time.localtime())
       

if __name__ == "__main__":
    app.run()
