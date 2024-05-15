FROM python:3
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=main
CMD ["flask", "run", "-h", "0.0.0.0"]
