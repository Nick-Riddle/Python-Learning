--SQL Views

USE [AdventureWorks2019]
GO;

CREATE VIEW [NumberCust]
AS
SELECT	COUNT([C].[CustomerID]) AS 'NumberCust',
		[C].[TerritoryId]
FROM [Sales].[Customer] AS [C]
GROUP BY [C].[TerritoryID]
GO;