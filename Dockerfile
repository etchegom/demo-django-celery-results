FROM python:3.7-buster

RUN pip install --upgrade pip

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait
RUN chmod +x /wait

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
CMD ["server"]
