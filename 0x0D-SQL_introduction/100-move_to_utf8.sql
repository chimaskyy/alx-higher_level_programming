-- converts database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci)
-- converts the Database hbtn_0c_0
-- first_table
-- and name field of first_table to utf8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
