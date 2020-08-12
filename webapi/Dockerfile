FROM python:3.6-alpine
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENV APPURL=http://apiserver:5000
EXPOSE 5000
ENTRYPOINT ["python", "webapi.py"]
