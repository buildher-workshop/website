#!/bin/bash

set -ex

./manage.py wait_for_database --stable 0
./manage.py migrate --noinput

exec "$@"
