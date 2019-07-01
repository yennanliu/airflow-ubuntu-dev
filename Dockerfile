FROM continuumio/miniconda3

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8
ENV LC_ALL en_US.UTF-8

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN /bin/bash -c "airflow initdb && airflow webserver -p 8088"
RUN /bin/bash -c "airflow worker "
RUN /bin/bash -c "airflow scheduler"
EXPOSE 8088
CMD ["python", "run.py"]