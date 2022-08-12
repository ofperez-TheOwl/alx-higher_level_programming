-- lists the `score` and number of occurances with each score with 'number'
-- displays this data sorted by number in descending order

SELECT score, name
	FROM second_table
	WHERE name IS NOT NULL AND name != ""
	ORDER BY score DESC;
