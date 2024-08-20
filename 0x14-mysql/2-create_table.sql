# Task 2
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
INSERT INTO nexus6(name) VALUES ('Leon');
SELECT * FROM nexus6;
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
