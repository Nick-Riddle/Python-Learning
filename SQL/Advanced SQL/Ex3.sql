--Ex.3

USE [WorldEvents];
GO

WITH cteID AS 
(
	SELECT [E].[CountryID]
	FROM [tblEvent] AS [E]
	WHERE 8 < (SELECT COUNT(*)
			   FROM [tblEvent] AS [ET]
			   WHERE [ET].[CountryID] = [E].[CountryID]
			   GROUP BY [ET].[CountryID])
	GROUP BY [E].[CountryID]
)

SELECT [C].[CountryName]
FROM [tblCountry] AS [C]
JOIN cteID AS [ID]
ON [ID].[CountryID] = [C].[CountryID]
ORDER BY [C].[CountryName];
