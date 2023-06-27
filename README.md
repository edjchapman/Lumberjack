Lumberjack Log Server
=====================

- Receives logs via REST API
- Logs can be searched, filtered analysed.
- Celery tasks to
  - Purge old logs
  - Issue alert summary emails if the number of logs exceeds the threshold for a given period

---
# Running Locally

## Docker
```shell
docker compose up
```
- Application served at http://0.0.0.0:8000/admin/logs/exceptionlog/
- Username: `testuser@lumberjacklogs.com`
- Password: `password`

## Non-Docker
```shell
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_database
python manage.py runserver
```

- Application served at http://0.0.0.0:8000/admin/logs/exceptionlog/
- Username: `testuser@lumberjacklogs.com`
- Password: `password`

---
# Screenshots

Log List

<h1 align="center">
  <br>
  <a href="https://lumberjacklogs.website/">
  <img src="https://github.com/edjchapman/Lumberjack/blob/main/.github/LogList.png" alt="Log List" />
</a>
</h1>

Log Detail

<h1 align="center">
  <br>
  <a href="https://lumberjacklogs.website/">
  <img src="https://github.com/edjchapman/Lumberjack/blob/main/.github/LogDetail.png" alt="Log Detail" />
</a>
</h1>

Surge Alert Email

<h1 align="center">
  <br>
  <a href="https://lumberjacklogs.website/">
  <img src="https://github.com/edjchapman/Lumberjack/blob/main/.github/SurgeAlertEmail.png" alt="Surge Alert Email" />
</a>
</h1>