FROM python:latest

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install 

CMD ["pipenv", "run", "uvicorn", "api.main:app", "--host=0.0.0.0"]
