FROM python:3.11.3-alpine AS buildprep


RUN python3 -m venv /tmp/task_table/venv
COPY requirements.txt /tmp/task_table/
RUN . /tmp/task_table/venv/bin/activate && \
pip --disable-pip-version-check --cache-dir /tmp/task_table/venv install -r /tmp/task_table/requirements.txt


COPY main.py /tmp/task_table/main.py
COPY pt.py /tmp/task_table/pt.py

FROM python:3.11.3-alpine
LABEL MAINTAINER="lonkaut@gmail.com"

COPY --from=buildprep /tmp/task_table /tmp/task_table


CMD source /tmp/task_table/venv/bin/activate && exec python3 -u /tmp/task_table/main.py
