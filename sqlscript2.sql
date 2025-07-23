USE jnec;
select * from sentences;

truncate table sentences;

ALTER TABLE sentences MODIFY COLUMN ParagraphNo VARCHAR(10);
ALTER TABLE sentences MODIFY COLUMN ParagraphSentenceIdx INT;
