FROM python:3.6-alpine


COPY . /usr/src/app

EXPOSE 5000

WORKDIR /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
