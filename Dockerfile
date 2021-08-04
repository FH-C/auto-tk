FROM python:3.7.11

RUN mkdir /app

RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& apt-get clean \
&& apt-get update
RUN apt install libopenjp2-7 -y
RUN apt install libtiff5 -y
RUN apt install tesseract-ocr -y

copy . /app

WORKDIR /app

ENV PUBLIC_KEY MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKf9iZkA5HEFw4zt7MRBkcmgUiz5+r5eqDOKbaurEbScmXd3ZZTtyzirqkYKRIH5mQ+8hq+Wd/pTZNXHS8L0+88CAwEAAQ==

RUN pip install -r requirements.txt

CMD ["python","main.py"]
