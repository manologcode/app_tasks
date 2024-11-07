FROM python:3.7

RUN apt-get update  -y

ENV TZ Europe/Madrid

WORKDIR /app

ENV PATH="/home/${USER}/app/.local/bin:${PATH}" 

RUN python -m pip install --upgrade pip

RUN pip install gunicorn

RUN pip install mysqlclient  
COPY ./app/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000