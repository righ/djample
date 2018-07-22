This is a django sample project, so it is named djample for short.

Besides it is considered the following:

- Docker deployment.

  - Local environment, you need just Docker and docker compose.
  - Container services which is like 'AWS ECS'.

- Webpack building.

  - VueJs (future support)
  - ReactJs (future support)

Local
=====

You can start local environment as follows

.. code-block:: shell

  $ docker-compose up

Login the app container as follows:

.. code-block:: shell

  $ docker exec -it djample_app_1 /bin/bash

.. code-block:: shell

  # activation
  root@local-djample:/home/www# source venv/bin/activate
  
  # move to apps dir
  (venv) root@local-djample:/home/www# cd djample/
  
  # start django shell
  (venv) root@local-djample:/home/www/djample# ./apps/manage.py shell
  Python 3.6.5 (default, Apr  1 2018, 05:46:30)
  [GCC 7.3.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>>
  
  # start django runserver
  Django version 2.0.7, using settings 'settings.local'
  Starting development server at http://0.0.0.0:8000/
  Quit the server with CONTROL-C.


Codes will shared with the component, it is automatically able to detect changes.

Production
==========

You are able to create images for production as follows:

.. code-block:: shell

  $ docker-compose -f docker-compose.prod.yml build --no-cache


.. note::

  If the following error appears,

  ::

    Building app
    Step 1/13 : FROM djample_base:latest
    ERROR: Service 'app' failed to build: pull access denied for djample_base, repository does not exist or may require 'docker login'

  you should make `djample_base` docker image before, the ways are as follows:

  - ``docker build . --no-cache``
  - ``docker-compose build # or up --no-cache``
