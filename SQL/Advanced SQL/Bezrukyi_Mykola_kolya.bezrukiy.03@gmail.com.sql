--Ex.1

USE [DoctorWho];
GO

SELECT [C].[CompanionName]
FROM [tblCompanion] AS [C]
FULL OUTER JOIN [tblEpisodeCompanion] AS [EC]
ON [C].CompanionId = [EC].CompanionId
WHERE [EC].CompanionId IS NULL;


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

SELECT [E].EventName,
	   [E].EventDate,
	   [C].CountryName 
FROM cteEvents AS [E]
JOIN [tblCountry] AS [C]
ON [E].[CountryID] = [C].[CountryID]
ORDER BY [E].[EventDate] DESC;


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


--Ex.4

USE [WorldEvents];
GO

WITH ThisAndThat AS 
(
	SELECT [E].[EventName], [E].[EventDetails],
		CASE 
			WHEN [E].[EventDetails] LIKE '%this%' THEN 1
			ELSE 0
		END AS 'IfThis',
		CASE
			WHEN [E].[EventDetails] LIKE '%that%' THEN 1
			ELSE 0
		END AS 'IfThat'
	FROM [tblEvent] AS [E]
)

SELECT [TAT].IfThis,
	   [TAT].IfThat,
	   COUNT(*) AS [Number of events]
FROM ThisAndThat AS [TAT]
GROUP BY [TAT].IfThis, [TAT].IfThat;

SELECT [TAT].[EventName],
	   [TAT].[EventDetails] 
FROM ThisAndThat AS [TAT]
WHERE [TAT].IfThis = 1 AND [TAT].IfThat = 1;


--Ex.5

USE [WorldEvents];
GO

WITH ManyCountries AS
(
	SELECT [C].[ContinentName],
		   COUNT([C].[ContinentID]) AS [Number of countries]
	FROM [tblContinent] AS [C]
	JOIN [tblCountry] AS [CT]
	ON [C].[ContinentID] = [CT].[ContinentID]
	GROUP BY [C].[ContinentName]
	HAVING COUNT([C].[ContinentID]) > 2
),
	FewEvents AS 
(
	SELECT [C].[ContinentName],
		   COUNT([C].[ContinentID]) AS [Number of events]
	FROM [tblContinent] AS [C]
	JOIN [tblCountry] AS [CT]
	ON [C].[ContinentID] = [CT].[ContinentID]
	JOIN [tblEvent] AS [E]
	ON [E].[CountryID] = [CT].[CountryID]
	GROUP BY [C].[ContinentName]
	HAVING COUNT([C].[ContinentID]) < 11
)

SELECT [FE].[ContinentName],
	   [MC].[Number of countries],
	   [FE].[Number of events]
FROM ManyCountries AS [MC]
JOIN FewEvents AS [FE]
ON [MC].[ContinentName] = [FE].[ContinentName];


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

SELECT [CE].[Era],
	   COUNT(*) AS [Number of events]
FROM cteEra AS [CE]
GROUP BY [CE].[Era];


--Ex.7

USE [DoctorWho];
GO

WITH cteEpisode AS
(
	SELECT YEAR([E].[EpisodeDate]) AS [EpisodeYear],
		   [E].[SeriesNumber],
		   [E].[EpisodeId]
	FROM [tblEpisode] AS [E]
)

SELECT [EpisodeYear],
	   [1],
	   [2],
	   [3],
	   [4],
	   [5]
FROM cteEpisode AS [E]
PIVOT(COUNT([E].[EpisodeId]) FOR [E].[SeriesNumber] IN ([1], [2], [3], [4], [5])) AS [EpisodePivot];

--Using dynamic SQL

DECLARE @table TABLE (
	[SeriesNumber] VARCHAR(20),
	[Rank] INT
);

INSERT INTO @table ([SeriesNumber],
					[Rank])
(
	SELECT DISTINCT [E].[SeriesNumber],
					DENSE_RANK() OVER (ORDER BY [E].[SeriesNumber]) AS 'Rank' 
	FROM [tblEpisode] AS [E]
);

DECLARE @i INT = 1
DECLARE @count INT =(SELECT COUNT(DISTINCT [E].[SeriesNumber]) 
					 FROM [tblEpisode] AS [E])
DECLARE @allseries VARCHAR (200) = ''

WHILE @i <= @count
BEGIN
	IF (@i != 1)
		SET @allseries = @allseries + ', '
	SET @allseries = @allseries + '[' + (SELECT [T].[SeriesNumber]
										 FROM @table AS [T]
										 WHERE [Rank] = @i)
								+ ']'
	SET @i = @i + 1
END

DECLARE @dynamicpivot VARCHAR(2000)
SET @dynamicpivot = 'SELECT [EpisodeYear], ' + @allseries
SET @dynamicpivot = @dynamicpivot + ' FROM (SELECT YEAR([E].[EpisodeDate]) AS [EpisodeYear], 
												   [E].[SeriesNumber], 
												   [E].[EpisodeId]
											FROM [tblEpisode] AS [E]) AS [ST]
									  PIVOT 
									  (
										 COUNT([ST].[EpisodeId]) FOR [ST].[SeriesNumber]
										 IN (' + @allseries + ')
									  ) AS [EpisodePivot]'

EXEC (@dynamicpivot)