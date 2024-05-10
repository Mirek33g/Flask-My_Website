FROM python:3
WORKDIR /code
COPY requirments.txt /code
RUN pip install -r requirments.txt
COPY . /code/