FROM python:3.6

RUN pip install zmq

COPY factory.py .

CMD [ "python", "factory.py" ]