# Prefequity website

A refreshed Django landing page for Prefequity, using the firm's existing copy with a more contemporary private-markets look.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Leave `DATABASE_URL` empty in `.env` to use SQLite at `db.sqlite3`. The `seed` command loads portfolio companies, news, team members and starter homepage carousel images.

Admin is available at `/admin/` after you create a superuser with `python manage.py createsuperuser`.

## Railway / production

1. Create a GitHub repo and connect it to a new Railway project.
2. Add a Railway **Postgres** plugin.
3. Copy the Postgres variables into `.env` using the Railway `KEY=value` format in [`.env.example`](.env.example). Locally, fill `DATABASE_PUBLIC_URL` (the proxy). Railway itself will inject `DATABASE_URL` on the private network.
4. Set `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for the public Railway domain.
5. Deploy. The release command runs migrations and collects static files.

Gunicorn serves the app. WhiteNoise serves static files. Uploaded media still lives on disk, so attach a Railway volume to `/app/media` if you need those files to persist.
