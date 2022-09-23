FROM python:3-slim --platform=linux/arm64,linux/arm/v7

RUN mkdir -v /app

WORKDIR /app

ADD ./connection-checker/connect.py .

RUN chmod a+x /app/connect.py

ENV CONNECT_ADDRESS="google.com"

ENV CONNECT_PORT='443'

ENV CONNECT_TIMEOUT_SECS='3'

ENV CONNECT_LOG_LEVEL='INFO'

CMD ["python", "/app/connect.py"]