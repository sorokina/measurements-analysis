FROM python:3.11.2-slim-buster



ENV HOME=/home/app
RUN mkdir -p $HOME

ENV APP_HOME=/home/app/code

RUN mkdir $APP_HOME

ENV DATA_DIR=/mnt/data
RUN mkdir $DATA_DIR

WORKDIR $APP_HOME

RUN python -m pip install pandas


COPY . $APP_HOME

ENTRYPOINT  ["python","app.py"]
