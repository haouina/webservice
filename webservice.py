#!/usr/bin/python2.7

import web
import platform
import config
import time


urls = (
    config.link, 'temps'
)
app = web.application(urls, globals())
dist = platform.linux_distribution()[0]
release = platform.linux_distribution()[1]


class temps:
    def GET(self, temps):
        try:
            if dist == 'Ubuntu' and release == '14.04':
                return time.strftime('Il est %H:%M:%S', time.localtime())
        except ValueError:
            print 'Error'
        finally:
            print 'You are not allowed to use this webservice'

if __name__ == "__main__":
    app.run()
