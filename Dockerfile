FROM python:3.11-slim-bookworm

COPY ./requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt

COPY . /peepapp-core
WORKDIR /peepapp-core

ENV PATH "${PATH}:/peepapp-core/peepapp_core/dexdump/"
