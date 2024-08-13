FROM python:3.12.1-bullseye
WORKDIR /app/
ADD . .
RUN pip install -r requirements.txt

CMD  [ "python", "wrapped/manage.py", "runserver", "0.0.0.0:8000" ]
EXPOSE 8000

