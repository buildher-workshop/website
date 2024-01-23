# buildher website

## Local development

```bash
docker compose --profile dev up --build
docker compose --profile dev exec django-dev ./manage.py createsuperuser
docker compose --profile dev exec django-dev ./manage.py loaddata demo
```

Install `pre-commit` as a git hook to commit clean code:

```bash
pre-commit install
```

## Fly.io deployment

1. Create the app with `fly launch`
  1. Create a Postgres database as well and write down the connection string
2. Set `DATABASE_URL` as secret
   1. Add `/postgres` to the connection string
   2. Run `fly secrets set DATABASE_URL=postgres//...`
3. Set the a random `SECRET_KEY` as secret
4. Run `fly deploy` to update the deployment
5. Create a superuser with `fly ssh console --pty -C "./manage.py createsuperuser"`
6. Load the initial data (if needed): `fly ssh console -C "./manage.py loaddata demo"`
