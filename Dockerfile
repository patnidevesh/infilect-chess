FROM python:3.11

WORKDIR /home/app
RUN pip install --upgrade pip
COPY . /home/app/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python3 manage.py runserver