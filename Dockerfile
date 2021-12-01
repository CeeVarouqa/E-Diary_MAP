FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache -r requirements.txt
COPY . .
CMD flask run --port 5555 --host 0.0.0.0
