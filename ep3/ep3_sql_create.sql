CREATE DATABASE IF NOT EXISTS django;
USE django;
CREATE TABLE IF NOT EXISTS class(
    id BIGINT NOT NULL ,
    title VARCHAR(20) NOT NULL,
    PRIMARY KEY(id)
)ENGINE =InnoDB DEFAULT CHARSET =UTF8;
CREATE TABLE IF NOT EXISTS student(
    id BIGINT NOT NULL ,
    name VARCHAR(20) NOT NULL,
    class_id BIGINT NOT NULL,
    PRIMARY KEY(id)
)ENGINE =InnoDB DEFAULT CHARSET=UTF8;
CREATE TABLE IF NOT EXISTS teacher(
    id BIGINT NOT NULL ,
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY(id)
)ENGINE =InnoDB DEFAULT CHARSET=UTF8;
CREATE TABLE IF NOT EXISTS link_t_C(
    id BIGINT NOT NULL ,
    teacher_id BIGINT NOT NULL,
    class_id BIGINT NOT NULL,
    PRIMARY KEY(id)
)ENGINE =InnoDB DEFAULT CHARSET=UTF8;
CREATE TABLE IF NOT EXISTS user_passwd(
    id BIGINT NOT NULL,
    email VARCHAR(20) NOT NULL,
    passwd VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX i_email (email)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8;
SHOW TABLES;
/* ALTER TABLE student ADD CONSTRAINT class_student_id FOREIGN KEY(class_id) REFERENCES class(id); */
/* ALTER TABLE link_t_C ADD CONSTRAINT class_class_id FOREIGN KEY(class_id) REFERENCES class(id); */
