#!/usr/bin/python2.7

import web
import datetime
import platform


urls = (
    '/(.*)', 'time'
)
app = web.application(urls, globals())

date = datetime.datetime.now()
dist = platform.linux_distribution()[0]
release = platform.linux_distribution()[1]


class time:
    def GET(self, time):
        try:
            if dist == 'Red Hat' and release == '6.0':
                return 'The Time is: ' + str(date)
        except ValueError:
            print 'Error'
        finally:
            print 'You are not allowed to use this webservice'

if __name__ == "__main__":
    app.run()
