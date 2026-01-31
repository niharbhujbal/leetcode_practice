# Write your MySQL query statement below
WITH RankedEmails AS (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM Person
)
DELETE FROM Person
WHERE id IN (
    SELECT id FROM RankedEmails WHERE rn > 1
);
