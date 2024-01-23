#!/bin/bash

set -ex

./manage.py wait_for_database --stable 0
./manage.py migrate --noinput
if ! ./manage.py shell -c "from django.conf import settings; exit(settings.DEBUG)"
then
    ./manage.py collectstatic --noinput
fi

exec "$@"
