--SQL XML grouping and ranking functions

USE [AdventureWorks2019]
GO;

SELECT	[PV].[ProductID],
		[PV].[AverageLeadTime],
		[PV].[MinOrderQty],
		[PV].[MaxOrderQty],
		[PV].[UnitMeasureCode],
		SUM([PV].[StandardPrice]) AS [SumPrice]
FROM [Purchasing].[ProductVendor] AS [PV]
GROUP BY ROLLUP
(
	[PV].[ProductID],
	[PV].[AverageLeadTime],
	[PV].[MinOrderQty],
	[PV].[MaxOrderQty],
	[PV].[UnitMeasureCode]
);

SELECT	[PV].[ProductID],
		[PV].[AverageLeadTime],
		[PV].[MinOrderQty],
		[PV].[MaxOrderQty],
		[PV].[UnitMeasureCode],
		SUM([PV].[StandardPrice]) AS [SumPrice]
FROM [Purchasing].[ProductVendor] AS [PV]
GROUP BY CUBE
(
	[PV].[ProductID],
	[PV].[AverageLeadTime],
	[PV].[MinOrderQty],
	[PV].[MaxOrderQty],
	[PV].[UnitMeasureCode]
);

SELECT	[PV].[ProductID],
		[PV].[AverageLeadTime],
		[PV].[MinOrderQty],
		[PV].[MaxOrderQty],
		[PV].[UnitMeasureCode],
		SUM([PV].[StandardPrice]) AS [SumPrice]
FROM [Purchasing].[ProductVendor] AS [PV]
GROUP BY GROUPING SETS
(
	[PV].[ProductID],
	([PV].[ProductID], [PV].[AverageLeadTime], [PV].[MinOrderQty], [PV].[MaxOrderQty], [PV].[UnitMeasureCode])
);