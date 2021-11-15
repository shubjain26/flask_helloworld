FROM python:3.8

RUN pip3 install flask==0.12.0

WORKDIR /app
COPY . /app

EXPOSE 8888

CMD python3 app.py