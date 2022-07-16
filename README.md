# FastAPI and Postgres
## Mac Terminal
```console
brew install postgresql
brew install --cask pgadmin4
brew install --cask postman # optional

python3 -m venv fastapi_postgresql_example
cd fastapi_postgresql_example
. bin/activate
pip install --upgrade pip (optional)
git clone <repo> <directory>
pip install -r requirements.txt
```

## common alembic command
```console
# for the first time
alembic init migration
alembic revision --autogenerate -m "Initial"

# or
alembic revision --autogenerate -m "drop books table"

# don't forget to update
alembic upgrade head
```
## common postgresql command
```console
brew install postgresql
brew services start postgresql
brew services stop postgresql
```

```sql
psql postgres

CREATE ROLE newUser WITH LOGIN PASSWORD ‘password’;
ALTER ROLE newUser CREATEDB;

\q
psql postgres -U newuser
```

## example setting
```Python
# .env
DB_USER=newuser
DB_PASSWORD=password
SECRET_KEY=abc123

# db.py
DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432/complaints"

# alembic.ini
sqlalchemy.url = postgresql://newuser:password@localhost:5432/clothes

# main.py
Debug Mode:
if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)
```
