FROM python:3.11


COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR src
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

