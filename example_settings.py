import os

env = os.environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.get("DB_NAME", default="example"),
        "USER": env.get("DB_USER", default=""),
        "PASSWORD": env.get("DB_PASSWORD", default=""),
        "HOST": env.get("DB_HOST", default=""),
        "PORT": env.get("DB_PORT", default=5432),
        "TEST": {"NAME": env.get("DB_TEST_NAME", default="example-test")},
    },
    "secondary": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.get("DB2_NAME", default="secondary"),
        "USER": env.get("DB2_USER", default=""),
        "PASSWORD": env.get("DB2_PASSWORD", default=""),
        "HOST": env.get("DB2_HOST", default=""),
        "PORT": env.get("DB2_PORT", default=5432),
        "TEST": {"NAME": env.get("DB2_TEST_NAME", default="example-secondary-test")},
    },
}
