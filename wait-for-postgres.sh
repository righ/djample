#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until psql -h "$host" -U "postgres" -c '\l' 2>/dev/null; do
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd