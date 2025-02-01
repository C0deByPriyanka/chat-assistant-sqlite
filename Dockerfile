FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python db_init.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

