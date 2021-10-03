FROM ubuntu:16.04

# Install required packages
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python 
RUN printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server 

RUN apt-get install -y python3-pip
RUN apt-get install nano
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN cat /etc/mysql/debian.cnf > /app/deb.txt
RUN service mysql start && python3 v2_for_docker.py
