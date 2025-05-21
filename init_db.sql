CREATE DATABASE IF NOT EXISTS test;
USE test;

CREATE TABLE IF NOT EXISTS submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    problem_slug VARCHAR(255),
    source_code TEXT,
    srclink VARCHAR(500),
    timestamp DATETIME
);
