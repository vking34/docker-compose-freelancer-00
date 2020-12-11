FROM python:3.8

RUN pip3 install pika==1.1.0
RUN pip3 install pyzmq==19.0.1
RUN pip install Flask
RUN pip install Flask-cors

WORKDIR /app
COPY . .

# for ZeroMQ server
#EXPOSE 5555
WORKDIR /app/rsa-calculator/calculator
#CMD python3 hello-world/hello.py


CMD python3 app.py