FROM python:3
ENV PYTHONUNBUFFERED 1

ADD . /src/
RUN pip install -r /src/requirements.txt

WORKDIR /src
ENTRYPOINT ./entrypoint.sh
