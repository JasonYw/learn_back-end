SHOW DATABASES;
USE py_write;
SHOW TABLES;
/* SELECT * FROM db_movie; */
SELECT name,score,date FROM db_movie ORDER BY score DESC,date DESC;
