FROM python:3.7

WORKDIR /code

RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Australia/Melbourne /etc/localtime \
    && rm /bin/sh \
    && ln -s /bin/bash /bin/sh \
    && python -m venv /venv

ADD requirements.txt .

RUN /bin/bash -c "source /venv/bin/activate && \
    pip install -r requirements.txt"
