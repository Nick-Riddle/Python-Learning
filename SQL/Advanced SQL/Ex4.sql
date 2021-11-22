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

SELECT [TAT].IfThis, [TAT].IfThat, COUNT(*) AS [Number of events]
FROM ThisAndThat AS [TAT]
GROUP BY [TAT].IfThis, [TAT].IfThat;

SELECT [TAT].[EventName], [TAT].[EventDetails] 
FROM ThisAndThat AS [TAT]
WHERE [TAT].IfThis = 1 AND [TAT].IfThat = 1;