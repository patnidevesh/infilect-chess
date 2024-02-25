FROM python:3.11

WORKDIR /home/app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000