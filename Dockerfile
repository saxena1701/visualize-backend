
FROM python:3.8-slim-buster

WORKDIR /animal-movement-visualizer

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY movement.csv movement.csv
COPY population.csv population.csv
COPY models.py models.py
COPY routes.py  routes.py
COPY main.py main.py 
COPY config.py config.py
COPY data_load.py data_load.py
COPY auth_routes.py auth_routes.py

ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=8000

EXPOSE 8000

CMD python3 -m flask --app main.py run --host=0.0.0.0 --port=8000