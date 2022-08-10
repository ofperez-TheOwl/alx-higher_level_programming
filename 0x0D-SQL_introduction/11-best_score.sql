-- list all records with [score >= 10] in descending order
-- from 'second_table' in given database

SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
