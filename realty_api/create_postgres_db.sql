CREATE DATABASE realty_db;
CREATE USER realty_admin WITH PASSWORD '1234';
ALTER ROLE realty_admin SET client_encoding TO 'utf8';
ALTER ROLE realty_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE realty_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE realty_db TO realty_admin;