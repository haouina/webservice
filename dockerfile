FROM appcontainers/centos:6

RUN yum update -y
RUN yum install -y python python-setuptools python-pip
RUN yum install -y wget
RUN wget http://webpy.org/static/web.py-0.37.tar.gz
RUN yum install -y tar.x86_64
RUN tar xvzf web.py-0.37.tar.gz
RUN cd web.py-0.37 && python setup.py install
RUN easy_install pytz
RUN pip install webservice

EXPOSE  8080

CMD ["/usr/bin/webservice.py"]

