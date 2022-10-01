FROM ubuntu:18.04

LABEL maintainer="dima@goltsman.net"

#install pip3
RUN apt update

RUN apt install -yqq python3-pip

#install python paho-mqtt client and urllib3
RUN pip3 install --upgrade pip setuptools  --no-cache-dir && \
    pip3 install paho-mqtt --no-cache-dir && \
    pip3 install urllib3 --no-cache-dir && \
    pip3 install loguru --no-cache-dir && \
    pip3 install apprise --no-cache-dir


ENV PYTHONIOENCODING=utf-8

ENV LANG=C.UTF-8

#Create working directory
RUN mkdir /opt/godaddy-ddns

ENV KEY ""
ENV SECRET ""
ENV SUBDOMAIN ""
ENV DOMAIN ""
ENV DOMAINS ""
ENV TTL 600
ENV RENEW_TIME 600

COPY godaddy_ddns.py /opt/godaddy-ddns

ENTRYPOINT ["/usr/bin/python3", "/opt/godaddy-ddns/godaddy_ddns.py"]