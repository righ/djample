FROM node:latest AS webpack
ARG webpack_config="webpack/webpack.prod.js"
ADD frontend/ frontend/
WORKDIR frontend/
RUN set -x  &&\
  npm install &&\
  $(npm bin)/webpack --config ${webpack_config}

FROM djample-base AS app
ARG requirements="requirements/requirements.txt"
WORKDIR /home/www
ADD apps/ apps/
ADD requirements/ requirements/
ADD static/ static/
RUN set -x &&\
  venv/bin/pip install -r ${requirements} &&\
  venv/bin/python apps/manage.py collectstatic --noinput --settings=settings.base

FROM nginx:perl
ADD deployment/nginx/uwsgi_params /etc/nginx/uwsgi_params
ADD deployment/nginx/nginx.conf /etc/nginx/nginx.conf
ADD deployment/nginx/conf.d/ /etc/nginx/conf.d/
COPY --from=app /home/www/static/ /usr/share/nginx/static/
COPY --from=webpack frontend/assets/ /usr/share/nginx/static/assets/

CMD ["nginx", "-g", "daemon off;"]
