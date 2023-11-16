-- creates a database hbtn_0d_2 and user 'user_0d_2'
-- user should have only SELECT privilege on datatbase

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
