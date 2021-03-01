-- changes database, table and field name to UTF9 encoding
-- utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE MyTable MODIFY MyColumn BINARY;
ALTER TABLE MyTable MODIFY MyColumn TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
