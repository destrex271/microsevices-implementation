FROM python:3.10.0-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && echo "OK"
EXPOSE 5000:5000
COPY . .
CMD flask --app ./server.py --debug run --host=0.0.0.0  

