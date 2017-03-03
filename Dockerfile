FROM alpine:3.5

MAINTAINER pstauffer@confirm.ch

ADD . /app

RUN apk --update upgrade && \
    apk add py2-openssl py2-pip ca-certificates && \
    apk add --no-cache --virtual=temporary curl gcc musl-dev linux-headers python-dev && \    
    curl "https://bootstrap.pypa.io/get-pip.py" | python && \
    pip install uwsgi && \
    apk del temporary && \
    rm -rf /var/cache/apk/* && \
    pip install -r /app/requirements.txt

ENV HOME /app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:app", "--processes", "1", "--threads", "8"]
