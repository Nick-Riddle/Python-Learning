--Ex.6

USE [WorldEvents];
GO

WITH cteEra AS 
(
	SELECT 
		CASE
			WHEN YEAR([E].[EventDate]) < 1900 THEN '19th century and earlier'
			WHEN YEAR([E].[EventDate]) < 2000 THEN '20th century'
			ELSE '21th century'
		END AS 'Era',
		[E].[EventID]
	FROM [tblEvent] AS [E]
)

SELECT [CE].[Era], COUNT(*) AS [Number of events]
FROM cteEra AS [CE]
GROUP BY [CE].[Era];

