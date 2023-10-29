FROM python:3.10.8-slim-buster
WORKDIR /mlproject
COPY . .
RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 8084
CMD ["python3", "application.py"]