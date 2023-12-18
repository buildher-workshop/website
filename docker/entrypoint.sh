#!/bin/bash

source $(poetry env info --path)/bin/activate

set -ex

./manage.py migrate --noinput
if ! ./manage.py shell -c "from django.conf import settings; exit(settings.DEBUG)"
then
    ./manage.py collectstatic --noinput
fi

exec "$@"
