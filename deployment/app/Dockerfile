FROM djample-base:latest
ARG requirements="requirements/requirements.txt"
ARG preprocess="echo start processing"
ARG project="djample"

USER www
RUN mkdir ${project}

WORKDIR /home/www/${project}
ADD apps/ apps/
ADD templates/ templates/
ADD static/ static/
ADD requirements/ requirements/

RUN set -x &&\
  ../venv/bin/pip install -r ${requirements}
 
CMD ${preprocess} && ../venv/bin/uwsgi --ini apps/uwsgi.ini
