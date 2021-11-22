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

SELECT [EpisodeYear], [1], [2], [3], [4], [5]
FROM cteEpisode AS [E]
PIVOT(COUNT([E].[EpisodeId]) FOR [E].[SeriesNumber] IN ([1], [2], [3], [4], [5])) AS [EpisodePivot];


--Using dynamic SQL

DECLARE @table TABLE (
	[SeriesNumber] VARCHAR(20),
	[Rank] INT
);

INSERT INTO @table ([SeriesNumber], [Rank])
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