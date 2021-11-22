--Ex.5

USE [WorldEvents];
GO

WITH ManyCountries AS
(
	SELECT [C].[ContinentName], COUNT([C].[ContinentID]) AS [Number of countries]
	FROM [tblContinent] AS [C]
	JOIN [tblCountry] AS [CT]
	ON [C].[ContinentID] = [CT].[ContinentID]
	GROUP BY [C].[ContinentName]
	HAVING COUNT([C].[ContinentID]) > 2
),
	FewEvents AS 
(
	SELECT [C].[ContinentName], COUNT([C].[ContinentID]) AS [Number of events]
	FROM [tblContinent] AS [C]
	JOIN [tblCountry] AS [CT]
	ON [C].[ContinentID] = [CT].[ContinentID]
	JOIN [tblEvent] AS [E]
	ON [E].[CountryID] = [CT].[CountryID]
	GROUP BY [C].[ContinentName]
	HAVING COUNT([C].[ContinentID]) < 11
)

SELECT [FE].[ContinentName], [MC].[Number of countries], [FE].[Number of events]
FROM ManyCountries AS [MC]
JOIN FewEvents AS [FE]
ON [MC].[ContinentName] = [FE].[ContinentName];