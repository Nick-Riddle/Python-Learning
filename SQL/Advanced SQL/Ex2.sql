--Ex.2

USE [WorldEvents];
GO

WITH cteEvents AS
(
	SELECT *
	FROM [tblEvent] AS [E]
	WHERE [E].[EventDate] >	(SELECT MAX([E].[EventDate])
							 FROM [tblEvent] AS [E]
							 WHERE [E].[CountryID] = 21)
)

SELECT [E].EventName, [E].EventDate, [C].CountryName 
FROM cteEvents AS [E]
JOIN [tblCountry] AS [C]
ON [E].[CountryID] = [C].[CountryID]
ORDER BY [E].[EventDate] DESC;