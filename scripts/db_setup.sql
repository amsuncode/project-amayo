-- script to create database and user so that django can connect
-- to postgresql db

CREATE DATABASE amayodb;
CREATE USER amayoadmin WITH ENCRYPTED PASSWORD '@_amayodev_#';
GRANT ALL PRIVILEGES ON DATABASE amayodb TO amayoadmin;