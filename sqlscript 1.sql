CREATE DATABASE IF NOT EXISTS jnec;
USE jnec;
CREATE TABLE IF NOT EXISTS sentences (
    id                    INT AUTO_INCREMENT PRIMARY KEY,
    `Index`               VARCHAR(10) NOT NULL,
    Sentence              TEXT        NOT NULL,
    ParagraphNo           VARCHAR(10) NOT NULL,
    ParagraphSentenceIdx  VARCHAR(10) NOT NULL
);
