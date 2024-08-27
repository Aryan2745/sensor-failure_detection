FROM python:3.12.0
FROM python:3.12.0
RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
CMD ["python","main.py"]