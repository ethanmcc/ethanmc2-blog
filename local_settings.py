
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "441cd266-099c-4aaf-9ae8-85d2a16d91365a42744b-535d-4bde-9e19-658e050fc69a415c4f8f-b55d-4f80-b1b3-34044d9bf6b8"
NEVERCACHE_KEY = "e406bc00-1148-4424-ad1c-f52833bbb7c983fa7c5e-42ae-4c96-a93b-50f823d858ba3610d215-efd3-43bd-b1de-8a802e2c40e1"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
