#!/bin/bash

source $(poetry env info --path)/bin/activate

set -ex

./manage.py migrate --noinput

exec "$@"
