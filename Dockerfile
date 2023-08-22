FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
COPY app.py /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
