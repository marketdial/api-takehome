FROM python:3.7-slim

RUN apt-get update && apt-get install postgresql curl -y
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["/bin/bash"]