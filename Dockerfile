FROM python:3.8

WORKDIR /contify

COPY ./app .

RUN pip install -r requirements.txt

ENTRYPOINT ["./gunicorn.sh"]
