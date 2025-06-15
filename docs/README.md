## PSQL command 

Those commands are used to create a user, create a db and give rights on this db to the created user.
```sql
psql -U postgres -c 'CREATE USER sakkz03 WITH PASSWORD 'evfyzjCyYskB3CguUh62CN6M7xd';'
psql -U postgres -c 'CREATE DATABASE repartition;'
psql -U postgres -d repartition -c "GRANT USAGE, CREATE ON SCHEMA public TO sakkz03;"
psql -U postgres -d repartition -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO sakkz03;"
psql -U postgres -d repartition -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO sakkz03;"

```