FROM python:3.7-slim
COPY . /code
RUN pip install --no-cache-dir -r /code/requirements.txt
EXPOSE 8000
WORKDIR /code
RUN python manage.py makemigrations 
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000

