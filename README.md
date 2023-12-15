```
django-admin startproject --template https://codeload.github.com/IlyaBulatau/django-template/zip/refs/heads/main settings
```

```
touch env/.env.dev && \
echo SECRET_KEY=super_key >> .env.dev && \
echo POSTGRES_NAME='database_name' >> .env.dev && \
echo POSTGRES_USER='postgres' >> .env.dev && \
echo POSTGRES_PASSWORD='postgres' >> .env.dev && \
echo POSTGRES_HOST='postgres' >> .env.dev && \
echo POSTGRES_PORT='5432' >> .env.dev
```

```
make migrate
```

```
make run
```
