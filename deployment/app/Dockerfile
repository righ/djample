FROM djample_base:latest
ARG requirements="requirements/requirements.txt"
ARG preprocess="echo start processing"
WORKDIR /home/www/
USER www

ADD apps/ apps/
ADD templates/ templates/
ADD static/ static/
ADD requirements/ requirements/

RUN set -x &&\
  venv/bin/pip install -r ${requirements}
 
CMD ${preprocess} && venv/bin/uwsgi --ini apps/uwsgi.ini
