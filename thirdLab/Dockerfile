FROM python:3.12.3

ENV PYTHONUNBUFFERED=1

WORKDIR /Projects

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]
